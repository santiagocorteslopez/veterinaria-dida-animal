filepath = r'C:\Users\santo\Desktop\paginas web\Clínica Veterinaria Vida Animal\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace gallery items
old1 = '<div class="gallery-item span-2 tall g1"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10h16v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8Z"/><path d="M9 10V7a3 3 0 0 1 6 0v3"/></svg><span>Sala de urgencias</span></div></div>'
new1 = '<div class="gallery-item span-2 tall g1"><div class="g-content"><img src="urgencias.png" alt="Sala de urgencias" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Sala de urgencias</span></div>'

old2 = '<div class="gallery-item g2"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3v6M6 6h10a4 4 0 0 1 0 8H6"/><circle cx="6" cy="18" r="3"/></svg><span>Quirófano</span></div></div>'
new2 = '<div class="gallery-item g2"><div class="g-content"><img src="cirugia.png" alt="Quirófano" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Quirófano</span></div>'

old3 = '<div class="gallery-item g3"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.35-9.5-8.5C.8 9.2 2.3 5.5 5.8 5c2-.3 3.6.8 4.6 2.2C11.4 8 12 9.5 12 9.5s.6-1.5 1.6-2.3c1-1.4 2.6-2.5 4.6-2.2 3.5.5 5 4.2 3.3 7.5C19 16.65 12 21 12 21z"/></svg><span>Consulta general</span></div></div>'
new3 = '<div class="gallery-item g3"><div class="g-content"><img src="consulta.png" alt="Consulta general" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Consulta general</span></div>'

old4 = '<div class="gallery-item g4"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 20h8M12 18v2"/></svg><span>Hospitalización</span></div></div>'
new4 = '<div class="gallery-item g4"><div class="g-content"><img src="hospitalizacion.png" alt="Hospitalización" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Hospitalización</span></div>'

old5 = '<div class="gallery-item span-2 g5"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 21c-2-3-1-7 2-9M17 21c2-3 1-7-2-9M12 3c1.5 1.5 1.5 4 0 5.5S10.5 4.5 12 3Z"/></svg><span>Área de estética canina</span></div></div>'
new5 = '<div class="gallery-item span-2 g5"><div class="g-content"><img src="estetica.png" alt="Estética canina" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Área de estética canina</span></div>'

old6 = '<div class="gallery-item g6"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l2-7 4 14 2-7h6"/></svg><span>Monitoreo clínico</span></div></div>'
new6 = '<div class="gallery-item g6"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l2-7 4 14 2-7h6"/></svg><span>Monitoreo clínico</span></div></div>'

old7 = '<div class="gallery-item g7"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg><span>Atención 24 horas</span></div></div>'
new7 = '<div class="gallery-item g7"><div class="g-content"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg><span>Atención 24 horas</span></div></div>'

old8 = '<div class="gallery-item span-2 tall g8"><div class="g-content"><img src="https://www.google.com/maps/place/CLINICA+VETERINARIA+VIDA+ANIMAL/@6.1691243,-75.5898356,3a,75y,90t/data=!3m8!1e2!3m6!1sCIABIhBNZ2bgnM04LqQog6koeD2O!2e10!3e12!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-cs-s%2FAHRPTWmDLvklJJXkqFw_Uy52pAxNi1s-hYwqWiby7BMHSQb-MgMSHPJyuYXKFxHfTBJD2yU2yIxvtyAT2OsZW_ak_ADyHf1QZHtiBuxkl55SienoGdsMlzkrpsVoW_rS6cbFoNYA56n4Zt4UHuWB%3Dw203-h270-k-no!7i3024!8i4032!4m7!3m6!1s0x8e468307f99548e1:0xaefb8cfd6dccd619!8m2!3d6.1691922!4d-75.5897508!10e5!16s%2Fg%2F11h3bhy6vp?entry=ttu&g_ep=EgoyMDI2MDkyMi4wIKXMDSoASAFQAw%3D%3D" alt="Clínica Vida Animal - Cirugía actualizada" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Cirugía</span></div>'
new8 = '<div class="gallery-item span-2 tall g8"><div class="g-content"><img src="https://www.google.com/maps/place/CLINICA+VETERINARIA+VIDA+ANIMAL/@6.1691243,-75.5898356,3a,75y,90t/data=!3m8!1e2!3m6!1sCIABIhBNZ2bgnM04LqQog6koeD2O!2e10!3e12!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-cs-s%2FAHRPTWmDLvklJJXkqFw_Uy52pAxNi1s-hYwqWiby7BMHSQb-MgMSHPJyuYXKFxHfTBJD2yU2yIxvtyAT2OsZW_ak_ADyHf1QZHtiBuxkl55SienoGdsMlzkrpsVoW_rS6cbFoNYA56n4Zt4UHuWB%3Dw203-h270-k-no!7i3024!8i4032!4m7!3m6!1s0x8e468307f99548e1:0xaefb8cfd6dccd619!8m2!3d6.1691922!4d-75.5897508!10e5!16s%2Fg%2F11h3bhy6vp?entry=ttu&g_ep=EgoyMDI2MDkyMi4wIKXMDSoASAFQAw%3D%3D" alt="Clínica Vida Animal - Cirugía" style="width:100%; height:100%; object-fit:cover; border-radius:16px;"></div><span>Cirugía</span></div>'

count = 0
replacements = [old1, old2, old3, old4, old5, old6, old7, old8]
new_list = [new1, new2, new3, new4, new5, new6, new7, new8]

for old, new in zip(replacements, new_list):
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"Replaced item {count}")
    else:
        print(f"Could not find: {old[:60]}...")

if count > 0:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nSuccessfully updated {count} gallery items!")
else:
    print("\nNo items were replaced.")