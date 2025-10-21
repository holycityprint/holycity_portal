from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from models import db
from . import purchasing_bp

# =====================================================
# === DASHBOARD PURCHASING ============================
# =====================================================
@purchasing_bp.route('/')
@login_required
def dashboard():
    """Dashboard utama modul Purchasing"""
    # Dummy data summary sementara (bisa diganti query DB)
    summary = {
        "supplier": 8,
        "open_po": 4,
        "received_today": 2,
        "month_value": 125_000_000
    }
    return render_template(
        "purchasing/dashboard.html",
        title="Dashboard Purchasing",
        user=current_user,
        summary=summary
    )

# =====================================================
# === DATA SUPPLIER ===================================
# =====================================================
@purchasing_bp.route("/suppliers")
@login_required
def suppliers():
    """Menampilkan daftar supplier (sementara dummy data)"""
    suppliers_data = [
        {
            "code": "SUP-001",
            "name": "PT Maju Jaya Abadi",
            "address": "Jl. Melati No.12 Jakarta Pusat",
            "phone": "021‑555‑1234",
            "email": "info@majujaya.id",
            "rating": 5
        },
        {
            "code": "SUP-002",
            "name": "CV Delta Mandiri",
            "address": "Jl. Jaksa No.8 Bandung",
            "phone": "022‑765‑4433",
            "email": "contact@delta.co.id",
            "rating": 4
        },
    ]
    return render_template(
        "purchasing/suppliers.html",
        title="Data Supplier",
        suppliers=suppliers_data,
        user=current_user,
    )

# =====================================================
# === PURCHASE ORDERS ================================
# =====================================================
@purchasing_bp.route("/orders", methods=["GET", "POST"])
@login_required
def orders():
    """Daftar dan form tambah purchase order"""
    if request.method == "POST":
        supplier = request.form.get("supplier")
        item = request.form.get("item")
        qty = request.form.get("quantity")
        price = request.form.get("price")

        if not all([supplier, item, qty, price]):
            flash("Lengkapi semua kolom sebelum menyimpan!", "warning")
        else:
            flash(
                f"Purchase order '{item}' ({qty} unit) untuk supplier '{supplier}' berhasil disimpan.",
                "success",
            )
        return redirect(url_for("purchasing.orders"))

    orders_data = [
        {
            "po": "PO‑2025‑015",
            "supplier": "PT Maju Jaya Abadi",
            "item": "Kertas A4 (500 lembar)",
            "qty": 50,
            "price": 55000,
            "status": "Approved",
            "date": "20/10/2025",
        },
        {
            "po": "PO‑2025‑016",
            "supplier": "CV Delta Mandiri",
            "item": "Tinta Printer",
            "qty": 20,
            "price": 72000,
            "status": "Draft",
            "date": "21/10/2025",
        },
    ]
    return render_template(
        "purchasing/orders.html",
        title="Purchase Orders",
        orders=orders_data,
        user=current_user,
    )

# =====================================================
# === PENERIMAAN BARANG ===============================
# =====================================================
@purchasing_bp.route("/receipts")
@login_required
def receipts():
    """Menampilkan daftar penerimaan barang"""
    receipts_data = [
        {
            "no": "GRN‑2025‑010",
            "po_no": "PO‑2025‑012",
            "supplier": "PT Mega Supply",
            "item": "Laptop ThinkBook 14",
            "qty_order": 5,
            "qty_receive": 5,
            "date": "19/10/2025",
            "status": "Validated",
        },
        {
            "no": "GRN‑2025‑011",
            "po_no": "PO‑2025‑008",
            "supplier": "PT Alfa Sarana",
            "item": "Mouse Wireless",
            "qty_order": 30,
            "qty_receive": 28,
            "date": "21/10/2025",
            "status": "Partially",
        },
    ]
    return render_template(
        "purchasing/receipts.html",
        title="Penerimaan Barang",
        receipts=receipts_data,
        user=current_user,
    )