import urllib.request, zipfile, io, os, shutil

URL = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"
os.makedirs("Data/Original", exist_ok=True)
print("Downloading official UCI Bike Sharing Dataset...")
data = urllib.request.urlopen(URL, timeout=60).read()
with zipfile.ZipFile(io.BytesIO(data)) as z:
    for name in ["hour.csv", "Readme.txt"]:
        with z.open(name) as src, open(os.path.join("Data/Original", name), "wb") as dst:
            shutil.copyfileobj(src, dst)
print("Done. Files saved in Data/Original/")
