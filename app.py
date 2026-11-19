import base64
import pandas as pd
import streamlit as st

import hashlib
from datetime import datetime, timezone
import streamlit as st

st.set_page_config(
    page_title="TWEVIX PULSE™ | Trust SHA-256 Audit & Credential Minter",
    page_icon="favicon.png",
    layout="wide",
)
with open("logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()



st.markdown(
    """
    <style>
    .stApp { background-color: #020617; color: #f8fafc; }
    .hero-banner {
        background: linear-gradient(135deg, rgba(167,139,250,0.18) 0%, #0f172a 70%);
        border: 1px solid rgba(167,139,250,0.4);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
    }
    .stButton > button, .stDownloadButton > button, .stLinkButton > a {
        background: #a78bfa !important;
        color: #020617 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def build_certificate_html(
    name: str,
    institution: str,
    cycle: str,
    track: str,
    issue_date: str,
    cred_id: str,
    sha256_hash: str,
) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>TWEVIX PULSE Verified Certificate - {name}</title>
<style>
  @page {{ size: A4 landscape; margin: 0; }}
  body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 32px; color: #0f172a; }}
  .cert-frame {{
    max-width: 960px; margin: 0 auto; background: #ffffff;
    border: 10px solid #0f172a; outline: 3px solid #10b981; outline-offset: -18px;
    padding: 48px 56px; box-shadow: 0 12px 30px rgba(0,0,0,0.08);
  }}
  .top-tag {{ font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #059669; }}
  h1 {{ font-size: 32px; margin: 10px 0 6px 0; color: #0f172a; }}
  .subtitle {{ font-size: 15px; color: #475569; margin-bottom: 24px; }}
  .recipient {{ font-size: 30px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #cbd5e1; display: inline-block; padding-bottom: 6px; margin: 8px 0; }}
  .institution {{ font-size: 16px; font-weight: 600; color: #334155; margin-bottom: 20px; }}
  .body-text {{ font-size: 15px; line-height: 1.6; color: #1e293b; max-width: 780px; }}
  .track-box {{ background: #ecfdf5; border-left: 5px solid #10b981; padding: 14px 20px; margin: 20px 0; font-size: 17px; font-weight: 700; color: #0f172a; }}
  .footer-grid {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: 32px; padding-top: 18px; border-top: 1px solid #e2e8f0; }}
  .sig-line {{ border-top: 1.5px solid #0f172a; width: 270px; padding-top: 6px; font-size: 13px; }}
  .hash-box {{ background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 10px 14px; font-family: monospace; font-size: 11px; color: #334155; max-width: 460px; word-break: break-all; }}
  @media print {{ body {{ background: #ffffff; padding: 0; }} .cert-frame {{ box-shadow: none; }} }}
</style>
</head>
<body>
  <div class="cert-frame">
    <div class="top-tag">TWEVIX™ • TWEVIX PULSE™ • CRYPTOGRAPHIC PROOF-OF-WORK LEDGER</div>
    <h1>Certificate of Audited Operational Proof-of-Work</h1>
    <div class="subtitle">Cryptographically Verified 12-Week (3-Month) Industry Deployment Credential</div>
    <div>This certifies that</div>
    <div class="recipient">{name}</div>
    <div class="institution">{institution}</div>
    <div class="body-text">
      Has successfully executed applied data diagnostics, decision-intelligence engineering, and quality-assured operational delivery under the supervision of <strong>TWEVIX PULSE™</strong> in the following verified deployment cycle:
    </div>
    <div class="track-box">{cycle} — {track}</div>
    <div class="footer-grid">
      <div class="sig-line">
        <strong>Willa Abraham</strong><br>
        MSc Data Science for Business (University of Stirling)<br>
        Founder &amp; Lead Product Architect, Twevix™
      </div>
      <div class="hash-box">
        <strong>CREDENTIAL ID:</strong> {cred_id} &nbsp;|&nbsp; <strong>ISSUED:</strong> {issue_date} UTC<br>
        <strong>SHA-256 FINGERPRINT:</strong><br>{sha256_hash}
      </div>
    </div>
  </div>
</body>
</html>"""
st.markdown(
    f"""
    <div style="display:flex;align-items:center;gap:16px;padding:8px 0 20px 0;">
        <img src="data:image/png;base64,{logo_b64}" style="width:62px;height:62px;border-radius:50%;border:2px solid #fbbf24;object-fit:cover;" />
        <div>
            <div style="font-size:26px;font-weight:900;letter-spacing:-0.02em;line-height:1.1;color:#f8fafc;">
                TWEVIX <span style="color:#fbbf24;">PULSE™</span>
            </div>
            <div style="font-size:12px;font-weight:700;letter-spacing:0.16em;color:#94a3b8;text-transform:uppercase;margin-top:4px;">
                VERIFIED TALENT • HR-TECH DIRECTORY
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-banner">
        <div style="color:#a78bfa;font-size:0.78rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;">
            TWEVIX PULSE™ • ZERO-TRUST CRYPTOGRAPHIC LEDGER
        </div>
        <h1 style="margin:0 0 8px 0;font-size:2rem;">Trust SHA-256 Audit &amp; Credential Minter</h1>
        <p style="color:#94a3b8;margin:0;max-width:760px;">
            Employers and institutions verify any TVX- credential ID by recomputing its SHA-256 signature, while supervisors issue tamper-evident proof-of-work certificates.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

TRACKS = [
    "Applied SME Margin & Waste Optimization Sprint",
    "Predictive Demand, Staffing & Operational Risk Modeling",
    "Anomaly Detection & Cold-Chain Governance Analytics",
    "Cross-Border Social-Impact Data Science Sprint",
]

CYCLES = [
    "Cycle 01 (3 Months)",
    "Cycle 02 (3 Months)",
    "Cycle 03 (3 Months)",
    "Cycle 04 (3 Months)",
]

col_audit, col_mint = st.columns(2)

with col_audit:
    st.subheader(":material/policy: Zero-Trust Employer Audit")
    st.write("Recompute the SHA-256 fingerprint of any TWEVIX PULSE™ certificate to confirm authenticity.")
    with st.form("audit_form"):
        a_name = st.text_input("Analyst Full Legal Name")
        a_inst = st.text_input("University / Institution")
        a_cycle = st.selectbox("Rotation Cycle", CYCLES)
        a_track = st.selectbox("Deployment Track", TRACKS)
        a_date = st.text_input("Issue Date (YYYY-MM-DD)", placeholder="2026-11-19")
        a_hash = st.text_input("Credential ID (TVX-...) or Full 64-Character SHA-256 Hash")
        audit_btn = st.form_submit_button("Verify Authenticity")

    if audit_btn:
        payload = f"{a_name.strip().upper()}|{a_inst.strip().upper()}|{a_cycle}|{a_track}|{a_date.strip()}|TWEVIX-PULSE-ENGINE"
        computed_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        computed_id = f"TVX-{computed_hash[:12].upper()}"
        if a_hash.strip().lower() == computed_hash or a_hash.strip().upper() == computed_id:
            st.success(f"VERIFIED AUTHENTIC: `{computed_id}` matches **{a_name.strip()}** ({a_cycle}).")
        else:
            st.error("AUDIT MISMATCH: Details do not match the cryptographic hash on file.")

with col_mint:
    st.subheader(":material/encrypted: Mint Rotation Credential (Supervisor)")
    st.write("Generate a new SHA-256 fingerprint and printable A4 certificate for a completed 3-month cycle.")
    with st.form("mint_form"):
        m_name = st.text_input("Learner Full Legal Name")
        m_inst = st.text_input("University / TVET")
        m_cycle = st.selectbox("Completed Rotation", CYCLES)
        m_track = st.selectbox("Deployment Track", TRACKS)
        m_key = st.text_input("Supervisor Passkey", type="password")
        mint_btn = st.form_submit_button("Mint SHA-256 Hash & Certificate")

    if mint_btn:
        expected_key = st.secrets.get("COHORT_KEY", "TWEVIX2026")
        if not m_name.strip() or not m_inst.strip():
            st.error("Please enter both Learner Name and Institution.")
        elif m_key != expected_key:
            st.error("Invalid Supervisor Passkey.")
        else:
            issue_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            raw_record = f"{m_name.strip().upper()}|{m_inst.strip().upper()}|{m_cycle}|{m_track}|{issue_date}|TWEVIX-PULSE-ENGINE"
            full_hash = hashlib.sha256(raw_record.encode("utf-8")).hexdigest()
            cred_id = f"TVX-{full_hash[:12].upper()}"

            st.success(f"Minted **{cred_id}** for **{m_name.strip()}** ({issue_date} UTC)")
            st.code(f"Credential ID: {cred_id}\nSHA-256 Hash: {full_hash}", language="text")

            cert_html = build_certificate_html(
                name=m_name.strip(),
                institution=m_inst.strip(),
                cycle=m_cycle,
                track=m_track,
                issue_date=issue_date,
                cred_id=cred_id,
                sha256_hash=full_hash,
            )
            st.download_button(
                label="Download Printable Certificate (Open & Save as PDF)",
                data=cert_html,
                file_name=f"TWEVIX_PULSE_Certificate_{m_name.strip().replace(' ', '_')}.html",
                mime="text/html",
            )

st.divider()
st.link_button("← Back to TWEVIX PULSE™ Home", "https://twevix.com")
