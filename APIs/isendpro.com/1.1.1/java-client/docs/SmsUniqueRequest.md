

# SmsUniqueRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateEnvoi** | **String** | Date d&#39;envoi au format YYYY-MM-DD hh:mm . Ce paramètre est optionnel, si il est omis l&#39;envoi est réalisé immédiatement. |  [optional] |
|**emetteur** | **String** | - L&#39;emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères.  - Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace.  - Il ne peut pas comporter uniquement des chiffres.   - Pour la modification de l&#39;émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d&#39;ajouter en fin de message le texte \&quot;STOP XXXXX\&quot;. De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.  |  [optional] |
|**gmtZone** | [**GmtZoneEnum**](#GmtZoneEnum) | Fuseau horaire de la date d&#39;envoi |  [optional] |
|**keyid** | **String** | Clé API |  |
|**nostop** | **String** | Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop &#x3D; \&quot;1\&quot; |  [optional] |
|**num** | **String** | Numero de téléphone au format national (exemple 0680010203) ou international (example 33680010203) |  |
|**numAzur** | [**NumAzurEnum**](#NumAzurEnum) |  |  [optional] |
|**sms** | **String** | Message à envoyer aux destinataires. Le message doit être encodé au format utf-8 et ne contenir que des caractères existant dans l&#39;alphabet GSM. Il est également possible d&#39;envoyer (à l&#39;étranger uniquement) des SMS en UCS-2, cf paramètre ucs2 pour plus de détails. |  |
|**smslong** | **String** | Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé.   Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong &#x3D; \&quot;999\&quot;  |  [optional] |
|**tracker** | **String** | Le tracker doit être une chaine alphanumérique de moins de 50 caractères. Ce tracker sera ensuite renvoyé en paramètre des urls pour les retours des accusés de réception.  |  [optional] |
|**ucs2** | **String** | Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 &#x3D; \&quot;1\&quot; Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.  |  [optional] |



## Enum: GmtZoneEnum

| Name | Value |
|---- | -----|
| PACIFIC_MIDWAY | &quot;Pacific/Midway&quot; |
| AMERICA_ADAK | &quot;America/Adak&quot; |
| ETC_GMT_10 | &quot;Etc/GMT+10&quot; |
| PACIFIC_MARQUESAS | &quot;Pacific/Marquesas&quot; |
| PACIFIC_GAMBIER | &quot;Pacific/Gambier&quot; |
| AMERICA_ANCHORAGE | &quot;America/Anchorage&quot; |
| AMERICA_ENSENADA | &quot;America/Ensenada&quot; |
| ETC_GMT_8 | &quot;Etc/GMT+8&quot; |
| AMERICA_LOS_ANGELES | &quot;America/Los_Angeles&quot; |
| AMERICA_DENVER | &quot;America/Denver&quot; |
| AMERICA_CHIHUAHUA | &quot;America/Chihuahua&quot; |
| AMERICA_DAWSON_CREEK | &quot;America/Dawson_Creek&quot; |
| AMERICA_BELIZE | &quot;America/Belize&quot; |
| AMERICA_CANCUN | &quot;America/Cancun&quot; |
| CHILE_EASTER_ISLAND | &quot;Chile/EasterIsland&quot; |
| AMERICA_CHICAGO | &quot;America/Chicago&quot; |
| AMERICA_NEW_YORK | &quot;America/New_York&quot; |
| AMERICA_HAVANA | &quot;America/Havana&quot; |
| AMERICA_BOGOTA | &quot;America/Bogota&quot; |
| AMERICA_CARACAS | &quot;America/Caracas&quot; |
| AMERICA_SANTIAGO | &quot;America/Santiago&quot; |
| AMERICA_LA_PAZ | &quot;America/La_Paz&quot; |
| ATLANTIC_STANLEY | &quot;Atlantic/Stanley&quot; |
| AMERICA_CAMPO_GRANDE | &quot;America/Campo_Grande&quot; |
| AMERICA_GOOSE_BAY | &quot;America/Goose_Bay&quot; |
| AMERICA_GLACE_BAY | &quot;America/Glace_Bay&quot; |
| AMERICA_ST_JOHNS | &quot;America/St_Johns&quot; |
| AMERICA_ARAGUAINA | &quot;America/Araguaina&quot; |
| AMERICA_MONTEVIDEO | &quot;America/Montevideo&quot; |
| AMERICA_MIQUELON | &quot;America/Miquelon&quot; |
| AMERICA_GODTHAB | &quot;America/Godthab&quot; |
| AMERICA_ARGENTINA_BUENOS_AIRES | &quot;America/Argentina/Buenos_Aires&quot; |
| AMERICA_SAO_PAULO | &quot;America/Sao_Paulo&quot; |
| AMERICA_NORONHA | &quot;America/Noronha&quot; |
| ATLANTIC_CAPE_VERDE | &quot;Atlantic/Cape_Verde&quot; |
| ATLANTIC_AZORES | &quot;Atlantic/Azores&quot; |
| EUROPE_BELFAST | &quot;Europe/Belfast&quot; |
| EUROPE_DUBLIN | &quot;Europe/Dublin&quot; |
| EUROPE_LISBON | &quot;Europe/Lisbon&quot; |
| EUROPE_LONDON | &quot;Europe/London&quot; |
| AFRICA_ABIDJAN | &quot;Africa/Abidjan&quot; |
| EUROPE_AMSTERDAM | &quot;Europe/Amsterdam&quot; |
| EUROPE_BELGRADE | &quot;Europe/Belgrade&quot; |
| EUROPE_BRUSSELS | &quot;Europe/Brussels&quot; |
| AFRICA_ALGIERS | &quot;Africa/Algiers&quot; |
| AFRICA_WINDHOEK | &quot;Africa/Windhoek&quot; |
| ASIA_BEIRUT | &quot;Asia/Beirut&quot; |
| AFRICA_CAIRO | &quot;Africa/Cairo&quot; |
| ASIA_GAZA | &quot;Asia/Gaza&quot; |
| AFRICA_BLANTYRE | &quot;Africa/Blantyre&quot; |
| ASIA_JERUSALEM | &quot;Asia/Jerusalem&quot; |
| EUROPE_MINSK | &quot;Europe/Minsk&quot; |
| ASIA_DAMASCUS | &quot;Asia/Damascus&quot; |
| EUROPE_MOSCOW | &quot;Europe/Moscow&quot; |
| AFRICA_ADDIS_ABABA | &quot;Africa/Addis_Ababa&quot; |
| ASIA_TEHRAN | &quot;Asia/Tehran&quot; |
| ASIA_DUBAI | &quot;Asia/Dubai&quot; |
| ASIA_YEREVAN | &quot;Asia/Yerevan&quot; |
| ASIA_KABUL | &quot;Asia/Kabul&quot; |
| ASIA_YEKATERINBURG | &quot;Asia/Yekaterinburg&quot; |
| ASIA_TASHKENT | &quot;Asia/Tashkent&quot; |
| ASIA_KOLKATA | &quot;Asia/Kolkata&quot; |
| ASIA_KATMANDU | &quot;Asia/Katmandu&quot; |
| ASIA_DHAKA | &quot;Asia/Dhaka&quot; |
| ASIA_NOVOSIBIRSK | &quot;Asia/Novosibirsk&quot; |
| ASIA_RANGOON | &quot;Asia/Rangoon&quot; |
| ASIA_BANGKOK | &quot;Asia/Bangkok&quot; |
| ASIA_KRASNOYARSK | &quot;Asia/Krasnoyarsk&quot; |
| ASIA_HONG_KONG | &quot;Asia/Hong_Kong&quot; |
| ASIA_IRKUTSK | &quot;Asia/Irkutsk&quot; |
| AUSTRALIA_PERTH | &quot;Australia/Perth&quot; |
| AUSTRALIA_EUCLA | &quot;Australia/Eucla&quot; |
| ASIA_TOKYO | &quot;Asia/Tokyo&quot; |
| ASIA_SEOUL | &quot;Asia/Seoul&quot; |
| ASIA_YAKUTSK | &quot;Asia/Yakutsk&quot; |
| AUSTRALIA_ADELAIDE | &quot;Australia/Adelaide&quot; |
| AUSTRALIA_DARWIN | &quot;Australia/Darwin&quot; |
| AUSTRALIA_BRISBANE | &quot;Australia/Brisbane&quot; |
| AUSTRALIA_HOBART | &quot;Australia/Hobart&quot; |
| ASIA_VLADIVOSTOK | &quot;Asia/Vladivostok&quot; |
| AUSTRALIA_LORD_HOWE | &quot;Australia/Lord_Howe&quot; |
| ETC_GMT_11 | &quot;Etc/GMT-11&quot; |
| ASIA_MAGADAN | &quot;Asia/Magadan&quot; |
| PACIFIC_NORFOLK | &quot;Pacific/Norfolk&quot; |
| ASIA_ANADYR | &quot;Asia/Anadyr&quot; |
| PACIFIC_AUCKLAND | &quot;Pacific/Auckland&quot; |
| ETC_GMT_12 | &quot;Etc/GMT-12&quot; |
| PACIFIC_CHATHAM | &quot;Pacific/Chatham&quot; |
| PACIFIC_TONGATAPU | &quot;Pacific/Tongatapu&quot; |
| PACIFIC_KIRITIMATI | &quot;Pacific/Kiritimati&quot; |



## Enum: NumAzurEnum

| Name | Value |
|---- | -----|
| _1 | &quot;1&quot; |



