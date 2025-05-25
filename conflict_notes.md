echo "# Decizie conflict feature-a vs feature-b  
Am ales să combin logica din ambele ramuri: funcția `calcul` returnează acum `(x + y) * 2`.  
Motiv: Pentru a evidenția modificările ambelor funcționalități." > conflict_notes.md

git add conflict_notes.md
git commit -m "Documentare decizie conflict"
git push origin feature-b   # Încarcă rezultatul pe GitHub