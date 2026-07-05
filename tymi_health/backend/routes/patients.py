from flask import Blueprint, request, jsonify
from db.custom_db import get_db_connection
from .groq_inference import get_triage_analysis

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients ORDER BY created_at DESC').fetchall()
    conn.close()
    return jsonify([dict(p) for p in patients])

@patients_bp.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    
    # Perform detailed AI analysis
    analysis = get_triage_analysis(data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO patients (
        name, age, address, phone, weight, height, bp, allergies, symptoms, 
        triage_status, recommendation, illness, scan_reports, medicines, 
        nutrition, hydration, rest, avoid, special_notes
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get('name'),
        data.get('age'),
        data.get('address'),
        data.get('phone'),
        data.get('weight'),
        data.get('height'),
        data.get('bp'),
        data.get('allergies'),
        data.get('symptoms'),
        analysis.get('triage_status'),
        analysis.get('recommendation'),
        analysis.get('illness'),
        analysis.get('scan_reports'),
        analysis.get('medicines'),
        analysis.get('nutrition'),
        analysis.get('hydration'),
        analysis.get('rest'),
        analysis.get('avoid'),
        analysis.get('special_notes')
    ))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"id": new_id, "analysis": analysis}), 201

@patients_bp.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    conn = get_db_connection()
    patient = conn.execute('SELECT * FROM patients WHERE id = ?', (id,)).fetchone()
    conn.close()
    if patient is None:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(dict(patient))
