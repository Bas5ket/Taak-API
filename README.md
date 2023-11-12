# taak-api

Mijn gekoze thema van mijn api is dungeons and dragons.<br />
Met de api kun je een user.<br />
Je kan ook een dnd character aan maken en ook de stats er bij zetten.<br />

## OpenAPI docs/Postman 
Voor de openapi docs en de postman gebruik ik de link van mijn gehoste api op okteto.<br />
Link: https://dnd-api-service-bas5ket.cloud.okteto.net/<br />
<br />
Hier kun u de screenshot van mijn OpenAPI docs<br />
![openapi docs](https://github.com/Bas5ket/taak-api/assets/75303668/9f38cdae-76f5-4646-9912-41aedbd45b4e)
link: https://dnd-api-service-bas5ket.cloud.okteto.net/docs<br />
<br />
Nu voor het deel van postman heb ik problemen met de post optie te gebruiken.<br />
![post users](https://github.com/Bas5ket/taak-api/assets/75303668/9f858d5c-e8d9-4c72-b730-6b3f7c36443f)
<br />
Ik weet niet dat het licht aan mijn code of dat ik postman verkeerd gebruik.<br />
Daarom ga ik de posts doen met OpenAPI docs.<br />
<br />
Dit is de post voor de users.<br />
![image](https://github.com/Bas5ket/taak-api/assets/75303668/b1ec2d7e-89d8-4b12-b85c-6ede76945117)
<br />
Dit is de post voor de character.<br />
![image](https://github.com/Bas5ket/taak-api/assets/75303668/3ab72d0c-1946-4453-8878-325d1c0f4274)
<br />
En dan als laatste de characters stats.<br />
![image](https://github.com/Bas5ket/taak-api/assets/75303668/2e0f411f-0673-424a-89b4-dd2b6629b976)
<br />
Nu dat ik het zo heb aangemaakt kunnen we wel met postman de get doen.<br />
<br />
Met de link https://dnd-api-service-bas5ket.cloud.okteto.net/users/1 kunnen we de users Opvragen met id 1<br />
![image](https://github.com/Bas5ket/taak-api/assets/75303668/464cbd01-46b1-4ac2-8c3e-7c2eb1f61663)
<br />
We kunnen dit ook op naam doen.<br />
Link: https://dnd-api-service-bas5ket.cloud.okteto.net/users/by_name/Stijn<br />
![image](https://github.com/Bas5ket/taak-api/assets/75303668/b6f69444-17d4-49a1-bf91-abf3e5e4dc09)
<br />
En ook op het email adres<br />
Link: https://dnd-api-service-bas5ket.cloud.okteto.net/users/by_email/test@test.be
![image](https://github.com/Bas5ket/taak-api/assets/75303668/316364b4-1d36-4387-91b6-53dfc2dd287b)
<br />
We kunnen ook de characters id doen een ook op de naam van de character.
Link voor character id: https://dnd-api-service-bas5ket.cloud.okteto.net/characters/1
![image](https://github.com/Bas5ket/taak-api/assets/75303668/1d569bcb-4005-4ea3-88a0-b4da39230db3)
<br />
Link voor character naam: https://dnd-api-service-bas5ket.cloud.okteto.net/characters/by_name/Velkhana frostfist
![image](https://github.com/Bas5ket/taak-api/assets/75303668/53722a10-cb28-4348-b7a2-51b533b7cbb2)
<br />
Ten laatste kunnen we ook de stats aanvragen.<br />
Dit gaat wel alleen maar op chracter stats id.<br />
link: https://dnd-api-service-bas5ket.cloud.okteto.net/characters_stats/1
![image](https://github.com/Bas5ket/taak-api/assets/75303668/eca84446-ce3b-45c1-9bad-b2dc41d1961f)
<br />




