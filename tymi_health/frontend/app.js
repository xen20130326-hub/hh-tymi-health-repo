async function loadPatients() {
    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/patients`);
        const patients = await response.json();
        
        const list = document.getElementById('patient-list');
        if (!list) return;
        
        list.innerHTML = '';
        let redCount = 0;
        
        patients.forEach(p => {
            if (p.triage_status?.toLowerCase() === 'red') redCount++;
            
            const row = document.createElement('tr');
            row.style.borderBottom = '1px solid #eee';
            const isSubfolder = window.location.pathname.includes('/pages/');
            const detailPath = isSubfolder ? `details.html?id=${p.id}` : `pages/details.html?id=${p.id}`;
            
            row.innerHTML = `
                <td style="padding: 10px 0;">${p.name}</td>
                <td>${p.age}</td>
                <td>${p.symptoms.substring(0, 30)}${p.symptoms.length > 30 ? '...' : ''}</td>
                <td><span class="triage-badge triage-${p.triage_status?.toLowerCase() || 'green'}">${p.triage_status || 'Green'}</span></td>
                <td><button onclick="window.location.href='${detailPath}'" class="btn" style="background: #eee;">View</button></td>
            `;
            list.appendChild(row);
        });
        
        document.getElementById('total-count').innerText = patients.length;
        document.getElementById('red-count').innerText = redCount;
    } catch (error) {
        console.error('Error loading patients:', error);
    }
}

async function addPatient(data) {
    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/patients`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (error) {
        console.error('Error adding patient:', error);
        return null;
    }
}

function viewDetails(id) {
    window.location.href = `pages/details.html?id=${id}`;
}

// Helper for relative paths if called from pages subfolder
function viewDetailsFromPage(id) {
    window.location.href = `details.html?id=${id}`;
}
