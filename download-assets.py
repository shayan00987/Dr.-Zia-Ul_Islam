"""Optional helper: download the distinct Unsplash images referenced in the website.
Run from the project root on a machine with internet access: python download-assets.py
Note: this helper downloads images but does not rewrite HTML references automatically.
"""
from pathlib import Path
from urllib.request import Request, urlopen

ASSETS = Path(__file__).parent / "assets"
IMAGES = {
    "clinic-interior.jpg": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1500&q=85",
    "calm-clinic.jpg": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=1500&q=85",
    "consultation.jpg": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1500&q=85",
    "facial-care.jpg": "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?auto=format&fit=crop&w=1000&q=85",
    "clinical-detail.jpg": "https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=1000&q=85",
    "medical-plan.jpg": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=1000&q=85",
    "treatment-room.jpg": "https://images.unsplash.com/photo-1551190822-a9333d879b1f?auto=format&fit=crop&w=1000&q=85",
    "consultation-room.jpg": "https://images.unsplash.com/photo-1512678080530-7760d81faba6?auto=format&fit=crop&w=1500&q=85",
    "wellness-space.jpg": "https://images.unsplash.com/photo-1511174511562-5f7f18b874f8?auto=format&fit=crop&w=1500&q=85",
    "patient-education.jpg": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=1200&q=85",
    "conversation.jpg": "https://images.unsplash.com/photo-1573497620053-ea5300f94f21?auto=format&fit=crop&w=1200&q=85",
    "healthcare-professional.jpg": "https://images.unsplash.com/photo-1579684453423-f84349ef60b0?auto=format&fit=crop&w=1200&q=85",
    "clinic-detail-2.jpg": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1500&q=85",
}
for filename, url in IMAGES.items():
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=30) as response:
            data = response.read()
        if len(data) < 10_000:
            raise RuntimeError("response too small to be an image")
        (ASSETS / filename).write_bytes(data)
        print(f"Saved {filename} ({len(data):,} bytes)")
    except Exception as exc:
        print(f"FAILED {filename}: {exc}")
