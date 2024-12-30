from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import DomainIP
from app.utils import resolve_domain
from app.forms import DomainForm

@app.route("/", methods=["GET", "POST"])
def home():
    form = DomainForm()
    if form.validate_on_submit():
        domain = form.domain.data
        ip_addresses, ipv6_addresses = resolve_domain(domain)

        if ip_addresses:
            # to save results to the database
            new_entry = DomainIP(domain=domain, ip_addresses=",".join(ip_addresses), ipv6_addresses=",".join(ipv6_addresses))
            db.session.add(new_entry)
            db.session.commit()

            return redirect(url_for("results", domain=domain))
        else:
            return render_template("index.html", form=form, error="Could not resolve domain.")

    return render_template("index.html", form=form)

@app.route("/results/<domain>")
def results(domain):
    entry = DomainIP.query.filter_by(domain=domain).first()
    return render_template("results.html", domain=domain, ip_addresses=entry.ip_addresses, ipv6_addresses=entry.ipv6_addresses)
