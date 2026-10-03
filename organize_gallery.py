filepath = r'C:\Users\santo\Desktop\paginas web\Clínica Veterinaria Vida Animal\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove g6, g7, g8 items and keep g1-g5
old_gallery = """<div class="gallery-grid">
      <div class="gallery-item span-2 tall g1"><div class="g-content"><img src="urgencias.png" alt="Sala de urgencias" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Sala de urgencias</span></div>
      <div class="gallery-item g2"><div class="g-content"><img src="cirugia.png" alt="Quirófano" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Quirófano</span></div>
      <div class="gallery-item g3"><div class="g-content"><img src="consulta.png" alt="Consulta general" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Consulta general</span></div>
      <div class="gallery-item g4"><div class="g-content"><img src="hospitalizacion.png" alt="Hospitalización" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Hospitalización</span></div>
      <div class="gallery-item span-2 g5"><div class="g-content"><img src="estetica.png" alt="Estética canina" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Área de estética canina</span></div>
      <div class="gallery-item g6"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l2-7 4 14 2-7h6"/></svg><span>Monitoreo clínico</span></div></div>
      <div class="gallery-item g7"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg><span>Atención 24 horas</span></div></div>
      <div class="gallery-item span-2 tall g8"><div class="g-content"><img src="https://www.google.com/maps/place/CLINICA+VETERINARIA+VIDA+ANIMAL/@6.1691243,-75.5898356,3a,75y,90t/data=!3m8!1e2!3m6!1sCIABIhBNZ2bgnM04LqQog6koeD2O!2e10!3e12!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-cs-s%2FAHRPTWmDLvklJJXkqFw_Uy52pAxNi1s-hYwqWiby7BMHSQb-MgMSHPJyuYXKFxHfTBJD2yU2yIxvtyAT2OsZW_ak_ADyHf1QZHtiBuxkl55SienoGdsMlzkrpsVoW_rS6cbFoNYA56n4Zt4UHuWB%3Dw203-h270-k-no!7i3024!8i4032!4m7!3m6!1s0x8e468307f99548e1:0xaefb8cfd6dccd619!8m2!3d6.1691922!4d-75.5897508!10e5!16s%2Fg%2F11h3bhy6vp?entry=ttu&g_ep=EgoyMDI2MDkyMi4wIKXMDSoASAFQAw%3D%3D" alt="Clínica Vida Animal - Cirugía" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Cirugía</span></div>
    </div>"""

new_gallery = """<div class="gallery-grid">
      <div class="gallery-item span-2 tall g1"><div class="g-content"><img src="urgencias.png" alt="Sala de urgencias" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Sala de urgencias</span></div>
      <div class="gallery-item g2"><div class="g-content"><img src="cirugia.png" alt="Quirófano" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Quirófano</span></div>
      <div class="gallery-item g3"><div class="g-content"><img src="consulta.png" alt="Consulta general" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Consulta general</span></div>
      <div class="gallery-item g4"><div class="g-content"><img src="hospitalizacion.png" alt="Hospitalización" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Hospitalización</span></div>
      <div class="gallery-item span-2 g5"><div class="g-content"><img src="estetica.png" alt="Estética canina" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Área de estética canina</span></div>
    </div>"""

if old_gallery in content:
    content = content.replace(old_gallery, new_gallery)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Gallery successfully updated! Removed g6, g7, g8 and kept g1-g5.")
else:
    print("Could not find the gallery section to replace")
    # Print first 200 chars to debug
    print("Content starts with:", content[:200])