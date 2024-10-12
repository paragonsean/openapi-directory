# ApiISendPro.SMSRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateEnvoi** | **String** | Paramètre optionnel, date d&#39;envoi au format YYYY-MM-DD hh:mm | [optional] 
**emetteur** | **String** | L&#39;emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. Il ne peut pas comporter uniquement des chiffres. Pour la modification de l’émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d’ajouter en fin de message le texte suivant : STOP XXXXX De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement. | [optional] 
**gmtZone** | **String** | Fuseau horaire de la date d&#39;envoi | [optional] 
**keyid** | **String** | Clé API | 
**nostop** | **String** | Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop &#x3D; \&quot;1\&quot; | [optional] 
**num** | **[String]** |  | 
**numAzur** | **String** |  | [optional] 
**repertoireId** | **String** | Id du repertoire | [optional] 
**sms** | **[String]** |  | 
**smslong** | **String** | Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé.   Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong &#x3D; \&quot;999\&quot;  | [optional] 
**tracker** | **[String]** |  | [optional] 
**ucs2** | **String** | Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 &#x3D; \&quot;1\&quot; Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères. | [optional] 



## Enum: GmtZoneEnum


* `Pacific/Midway` (value: `"Pacific/Midway"`)

* `America/Adak` (value: `"America/Adak"`)

* `Etc/GMT+10` (value: `"Etc/GMT+10"`)

* `Pacific/Marquesas` (value: `"Pacific/Marquesas"`)

* `Pacific/Gambier` (value: `"Pacific/Gambier"`)

* `America/Anchorage` (value: `"America/Anchorage"`)

* `America/Ensenada` (value: `"America/Ensenada"`)

* `Etc/GMT+8` (value: `"Etc/GMT+8"`)

* `America/Los_Angeles` (value: `"America/Los_Angeles"`)

* `America/Denver` (value: `"America/Denver"`)

* `America/Chihuahua` (value: `"America/Chihuahua"`)

* `America/Dawson_Creek` (value: `"America/Dawson_Creek"`)

* `America/Belize` (value: `"America/Belize"`)

* `America/Cancun` (value: `"America/Cancun"`)

* `Chile/EasterIsland` (value: `"Chile/EasterIsland"`)

* `America/Chicago` (value: `"America/Chicago"`)

* `America/New_York` (value: `"America/New_York"`)

* `America/Havana` (value: `"America/Havana"`)

* `America/Bogota` (value: `"America/Bogota"`)

* `America/Caracas` (value: `"America/Caracas"`)

* `America/Santiago` (value: `"America/Santiago"`)

* `America/La_Paz` (value: `"America/La_Paz"`)

* `Atlantic/Stanley` (value: `"Atlantic/Stanley"`)

* `America/Campo_Grande` (value: `"America/Campo_Grande"`)

* `America/Goose_Bay` (value: `"America/Goose_Bay"`)

* `America/Glace_Bay` (value: `"America/Glace_Bay"`)

* `America/St_Johns` (value: `"America/St_Johns"`)

* `America/Araguaina` (value: `"America/Araguaina"`)

* `America/Montevideo` (value: `"America/Montevideo"`)

* `America/Miquelon` (value: `"America/Miquelon"`)

* `America/Godthab` (value: `"America/Godthab"`)

* `America/Argentina/Buenos_Aires` (value: `"America/Argentina/Buenos_Aires"`)

* `America/Sao_Paulo` (value: `"America/Sao_Paulo"`)

* `America/Noronha` (value: `"America/Noronha"`)

* `Atlantic/Cape_Verde` (value: `"Atlantic/Cape_Verde"`)

* `Atlantic/Azores` (value: `"Atlantic/Azores"`)

* `Europe/Belfast` (value: `"Europe/Belfast"`)

* `Europe/Dublin` (value: `"Europe/Dublin"`)

* `Europe/Lisbon` (value: `"Europe/Lisbon"`)

* `Europe/London` (value: `"Europe/London"`)

* `Africa/Abidjan` (value: `"Africa/Abidjan"`)

* `Europe/Amsterdam` (value: `"Europe/Amsterdam"`)

* `Europe/Belgrade` (value: `"Europe/Belgrade"`)

* `Europe/Brussels` (value: `"Europe/Brussels"`)

* `Africa/Algiers` (value: `"Africa/Algiers"`)

* `Africa/Windhoek` (value: `"Africa/Windhoek"`)

* `Asia/Beirut` (value: `"Asia/Beirut"`)

* `Africa/Cairo` (value: `"Africa/Cairo"`)

* `Asia/Gaza` (value: `"Asia/Gaza"`)

* `Africa/Blantyre` (value: `"Africa/Blantyre"`)

* `Asia/Jerusalem` (value: `"Asia/Jerusalem"`)

* `Europe/Minsk` (value: `"Europe/Minsk"`)

* `Asia/Damascus` (value: `"Asia/Damascus"`)

* `Europe/Moscow` (value: `"Europe/Moscow"`)

* `Africa/Addis_Ababa` (value: `"Africa/Addis_Ababa"`)

* `Asia/Tehran` (value: `"Asia/Tehran"`)

* `Asia/Dubai` (value: `"Asia/Dubai"`)

* `Asia/Yerevan` (value: `"Asia/Yerevan"`)

* `Asia/Kabul` (value: `"Asia/Kabul"`)

* `Asia/Yekaterinburg` (value: `"Asia/Yekaterinburg"`)

* `Asia/Tashkent` (value: `"Asia/Tashkent"`)

* `Asia/Kolkata` (value: `"Asia/Kolkata"`)

* `Asia/Katmandu` (value: `"Asia/Katmandu"`)

* `Asia/Dhaka` (value: `"Asia/Dhaka"`)

* `Asia/Novosibirsk` (value: `"Asia/Novosibirsk"`)

* `Asia/Rangoon` (value: `"Asia/Rangoon"`)

* `Asia/Bangkok` (value: `"Asia/Bangkok"`)

* `Asia/Krasnoyarsk` (value: `"Asia/Krasnoyarsk"`)

* `Asia/Hong_Kong` (value: `"Asia/Hong_Kong"`)

* `Asia/Irkutsk` (value: `"Asia/Irkutsk"`)

* `Australia/Perth` (value: `"Australia/Perth"`)

* `Australia/Eucla` (value: `"Australia/Eucla"`)

* `Asia/Tokyo` (value: `"Asia/Tokyo"`)

* `Asia/Seoul` (value: `"Asia/Seoul"`)

* `Asia/Yakutsk` (value: `"Asia/Yakutsk"`)

* `Australia/Adelaide` (value: `"Australia/Adelaide"`)

* `Australia/Darwin` (value: `"Australia/Darwin"`)

* `Australia/Brisbane` (value: `"Australia/Brisbane"`)

* `Australia/Hobart` (value: `"Australia/Hobart"`)

* `Asia/Vladivostok` (value: `"Asia/Vladivostok"`)

* `Australia/Lord_Howe` (value: `"Australia/Lord_Howe"`)

* `Etc/GMT-11` (value: `"Etc/GMT-11"`)

* `Asia/Magadan` (value: `"Asia/Magadan"`)

* `Pacific/Norfolk` (value: `"Pacific/Norfolk"`)

* `Asia/Anadyr` (value: `"Asia/Anadyr"`)

* `Pacific/Auckland` (value: `"Pacific/Auckland"`)

* `Etc/GMT-12` (value: `"Etc/GMT-12"`)

* `Pacific/Chatham` (value: `"Pacific/Chatham"`)

* `Pacific/Tongatapu` (value: `"Pacific/Tongatapu"`)

* `Pacific/Kiritimati` (value: `"Pacific/Kiritimati"`)





## Enum: NumAzurEnum


* `1` (value: `"1"`)




