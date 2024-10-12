/*
 * PhantAuth
 * Random User Generator + OpenID Connect Provider. Like Lorem Ipsum, but for user accounts and authentication.  The PhantAuth API documentation is available on the following API documentation sites:  - [apiary](https://phantauth.docs.apiary.io) (primary source)  - [speca](https://speca.io/phantauth/phantauth)  - [PhantAuth Developer Portal](https://www.phantauth.net/api)  ### TL;DR  **PhantAuth was designed to simplify testing for applications using OpenID Connect authentication by making use of random generated users.**  endpoint  | address --------- | ------- issuer    | https://phantauth.net discovery | https://phantauth.net/.well-known/openid-configuration  credential    | value ------------- | ----- client_id     | test.client client_secret | UTBcWwt5  ## OpenID Connect  The OpenID Connect Provider of PhantAuth supports the flows listed in the OpenID Connect specifications (Hybrid, Implicit, Authorization Code), as well as the Resource Owner Password grant type, specified in the OAuth 2.0 specifications. PhantAuth as an OpenID Connect Provider can be integrated with a variety of web applications, mobil applications, and  backend applications. The integration can be either direct, as in the case of the OpenID Connect Provider, or through an authentication integration service, as in the case of Auth0 or Azure Active Directory B2C. To learn more, please go to chapter [Integration](https://doc.phantauth.net/#/integration).  Examples:  - [Direct OpenID Connect integration](https://www.phantauth.net/test/oidc)  - [Auth0 Social Connections integration](https://www.phantauth.net/test/auth0)  - [Azure Active Directory B2C integration](https://www.phantauth.net/test/azure)  ## Random User  The random user generator of PhantAuth can also be used separately, independent of the OpenID Connect Provider. You can generate an optional number of test users. In the knowledge of their user name, the data of the generated users can be regenerated at any time (OpenID Connect *sub* claim). The generated users have a unique, operational, disposable email address, a profile picture selected from one of the multiple pools of pictures, and the usual profile data. Custom email addresses and profile pictures may also be added. The random user generator of PhantAuth can be fully customized. Additionally, you can link an external generator to the application. For details,please go to chapter [Generator](https://doc.phantauth.net/#/generator).  Test pages:  - [Default Generator Test Page](https://phantauth.net/test/user) (embedded generator)  - [Greek Gods Generator Test Page](https://phantauth.net/_gods/test/user) (embedded generator working from a Google Sheet)  - [Faker Generator Test Page](https://phantauth.net/_faker/test/user) (external generator using Javascript Faker library)  - [Chance Generator Test Page](https://phantauth.net/_chance/test/user) (external generator using Javascript Chance library)  - [Casual Generator Test Page](https://phantauth.net/_casual/test/user) (external generator using Javascript Casual library)  - [Randomuser Generator Test Page](https://phantauth.net/_randomuser/test/user) (client side generator using https://randomuser.me)  - [uinames Generator Test Page](https://phantauth.net/_uinames/test/user) (client side generator using https://uinames.com)  - [Mockaroo Generator Test Page](https://phantauth.net/_mockaroo/test/user) (client side generator using https://mockaroo.com)  Every random generated user has a profile page, which contains their profile data in a simple one-page format.  Profile examples:  - [Random Profile](https://phantauth.net/%7Ejoe.black)  - [Random Greek God Profile](https://phantauth.net/_gods/%7Ezeus)  - [Random Faker Profile](https://phantauth.net/_faker/%7Eharry.houdini)  - [Random Chance Profile](https://phantauth.net/_chance/%7Epeter.pan)  - [Random Casual Profile](https://phantauth.net/_casual/%7Ejohn.smith)  ## CodeSandbox  The use of the random user generator and the direct integration of  the OpenID Connect is demonstrated through a set of CodeSandbox samples. The sample applications are run directly from CodeSandbox, so the source code is easy to view, edit, and test.  Examples:  - [Random User Generator usage exampe](https://4xyj8lw394.codesandbox.io/)  - [OpenID Connect direct integration exampe](https://8z77681269.codesandbox.io/)  ## Tenants  The PhantAuth is extremely versatile and customizable. You can use your own random user service, or generate users from an external .csv file or Google Sheet. You can use a set of Bootstrap themes to tailor the look and feel of the profile, morover, you can fundamentally change the same look and feel by the use of your own HTML templates. To find out more, please go to chapter [Tenant](https://doc.phantauth.net/#/tenant).  To customize the application, you need to use one or more so-called tenants. A tenant can be consiered as an independent PhantAuth service. A tenant has its own random user generator endpoints and OpenID Connect endpoints.  The tenants can be organised into so-called domains. Practically, a domain is a DNS zone, which contains the settings of the given tenant(s). The tenants as well as the domain can be configured by the use of DNS TXT records.  In addition to the default tenant, the PhantAuth domain contains some sample tenants, which are primarily designed to demonstrate customizability, a range of hosting possibilities, and the links to external services. In most cases, using the [default tenant](https://phantauth.net) is enough.  - [PhantAuth Default](https://phantauth.net) - default tenant, based on a Java Fairy library  - [Greek Gods](https://phantauth.net/_gods) - based on a Google Sheet document  - [PhantAuth Faker](https://phantauth.net/_faker) - based on a Javascript Faker library, hosted at https://now.sh  - [PhantAuth Chance](https://phantauth.net/_chance) - based on a Javascript Chance library, hosted at https://now.sh  - [PhantAuth Casual](https://phantauth.net/_casual) - based on a Javascript Casual library, hosted at https://webtask.io  - [RANDOM USER](https://phantauth.net/_randomuser) - based on https://randomuser.me service  - [uinames](https://phantauth.net/_uinames) - based on https://uinames.com service  - [Mockaroo](https://phantauth.net/_mockaroo) - based on  https://mockaroo.com service  Anyone can create a domain and the tenants. Sharing the tenants is facilitated by the [PhantAuth Shared Domain](https://shared.phantauth.net). A shared domain is connected to the [phantauth.cf](http://phantauth.cf) DNS zone, where anyone can create tenant configuration nodes by the use of the [FreeDNS](https://freedns.afraid.org/) service.  ### Concept  The internal structure of PhantAuth is modular enough to allow certain elements to be customized or even replaced. The customized PhantAuth instances can be considered as separate services, which are independent from the original one. For the sake of simplicity, the customized PhantAuth instances will be called **tenants**.  The customized PhantAuth instances (tenants) have a different URL from that of the default tenant. For technological and cloud hosting purposes, it is advised that only the beginning of the path component of these URLs differs from the default PhantAuth URL. Similarly, the path component of a tenant URL should start with a low line character (\"_\"). So the general format of a tenant URL is:  ``` https://phantauth.net/_TENANT ```  where `TENANT` is the name of the tenant. The tenant name is a DNS domain name at the same time, which may lack `.phantauth.net` or `.phantauth.cf` from the end.  ### DNS for configuration  When desiging PhantAuth, the aim is that PhantAuth can run without a database, and it is configurable by the users. This can be achieved if for the purpose of storing the tenant configuration, the system uses the special TXT records of the Domain Name System (DNS), in compliance with the [RFC 6763](https://tools.ietf.org/html/rfc6763) specifications. So the tenant name is one or more DNS TXT records. These TXT records contain the configuration properties in NAME=VALUE format.  This allows anyone to create their own tenants by creating a DNS domain and the TXT records in that domain. [Freenom](https://www.freenom.com), a service provider, allows you to register some top-level domains (.tk, .ml, .ga, .cf, .gq) free charge. The domain registered this way can be managed on the online interface of Freenom or transferred to an other free service provider offering a more convenient DNS name server (e.g. [CloudFlare](https://www.cloudflare.com/)). Additionally, [FreeDNS](https://freedns.afraid.org/) allows you to create DNS records within a second- or third level domain that is privately owned or shared with a community. In this case, you are advised to create the entries within the `phantauth.cf` domain, because here you can omit the `.phantauth.cf` from the tenant name in the URL. This means that a tenant with a name of `mytenant.phantauth.cf` can be referred to in the shorther `https://phantauth.net/_mytenant` format, rather than the longer `https://phantauth.net/_mytenant.phantauth.cf` URL . Similar to `.phantauth.cf`, the `phantauth.net` can be omitted, thus the officially supported and the example tenants can be referred to by their short names (e.g. https://phantauth.net/_faker).  In a nutshell, to create a tenant, you have the following options:  - With TXT records in a domain registered at Freenom, either on the online interface of Freenom or that of another free DNS service provider (e.g. CloudFlare).  - With TXT records created in a second- or third level domain shared with a community, by using FreeDNS.  - With TXT records created in your own existing DNS domain, by the use of an any DNS software.  ### Parameters  The below table contains a summary of the tenant parameters having an effect on the operation of the tenants.  Property | Description --- | --- [name](#name) | the displayed name of the tenant [flags](#flags) | generator flags having an effect on the login page [theme](#theme) | the address of the Bootstrap theme [template](#template) | the address of the HTML page templates [factory](#factory) | the address of the external user generator [depot](#depot) | the address of the external user database [sheet](#sheet) | the identifier of the Google Sheets document containing the user database [script](#script) | the JavaScript URL inserted in the HTML pages [summary](#summary) | a one-line summary of the tenant [about](#about) | a detailed description of the tenant [attribution](#attribution) | the specifications of the external source [logo](#logo) | the logo of the tenant [favicon](#favicon) | the favicon of the tenant's web pages  #### name  The displayed name of the tenant is defined in the `name` parameter. In lack of such a name, the tenant's DNS name is displayed. This name appears in the address bar of the tenant's webpages.  #### flags  This parameter contains the flags that affect the operation of a tenant (see [Flags](generator.md#flags)). Currently, the flags affecting the team size are used in the login screen. If any of the flags is a team size flag, you can select the user from a list in the login screen, rather than using an input field. It can take the following values:  - tiny  - small  - medium  - large  #### theme  The HTML page templates of a tenant are created by the use of the Bootstrap library. This allows you to customize the layout and the colours of the pages by using external Bootstrap CSS files. The `theme` parameter contains the URL of the Bootstrap CSS file used in the pages. It is optional; in lack of such a parameter, the tenant's HTML pages have the default layout provided in the [PhantAuth developer portal](https://www.phantauth.net).  #### template  The place of the HTML page templates of a tenant is specified by the `template` parameter. The value of the parameter is n [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) expression. The URI template receives the page name in a `resource` parameter.  The default value of the `template` parameter:  ``` https://default.phantauth.net{/resource} ```  The `resource` URI template parameter may take the following values:  Value | Description --- | --- tenant.html | the tenant's webpage; it contains a short description and the entry points of the tenant  user.html | the user's profile page login.html | the login page used for signing in consent.html | the content page used for signing in team.html | the profile page of the user group client.html | the profile page of a client fleet.html | the profile page of the client group policy.html | the client's privacy policy tos.html | a client's terms of service test.html | a login test page of the user generator and OpenID Connect  If you use your own template, the pages are fully customizable. The templates use a template engine called [Thymeleaf](https://www.thymeleaf.org/), which provides flexible template options. The source of the default template is available in the [phantauth-default](https://github.com/phantauth/phantauth-default) GitHub repository. If you wish to create your own templates, you are advised to produce them from these templates.  #### factory  PhantAuth allows you to use your own random resource (user, team) generator. To do so, you need to provide its address in the `factory` tenant parameter. The value of the parameter is an [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) expression. The URI template receives the type of the object (user, team) to be generated in the `kind` parameter, and the identifier of the object to be generated in the `name` parameter.  #### factories  In the `factories` parameter, you can specify the resource types that can be generated by the external generator set in the `factory` parameter. It takes the value of one or more strings from the following: `user`, `team`.  #### depot  Instead of generating a user and team resource, you can randomly select them from a pre-created inventory. In this case, the URL of the CSV file containing the resources can be specified in the `depot` parameter. The value of the parameter is an [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) expression. The URI template receives the type of the object (user, team) to be generated in the `kind` parameter.  The first line of the CSV file contains the resource property names, the following lines, on the other hand, contain the relevant data. In the case of nested properties, a \".\" character separates the elements of the property name (e.g. address.formatted).  #### depots  In the `depots` parameter, you can specify the purpose of the external source set in the `depot` parameter. It takes the value of one or more strings from the following: `user`, `team`.  #### sheet  You can randomly select the user data from a Google Sheets document. In the `sheet` parameter, you can specify the identifier of a public Google Sheets document. The first row of the table contains the user property names, the following rows contain the relating data. In the case of nested properties, a \".\" character is used to separate the elements of the property name (e.g. address.formatted).  The tenant named `gods` is an example for the use of the `sheet` parameter. It provides the user data in a [public Google Sheets](https://docs.google.com/spreadsheets/d/1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY/) document. In this case, the identifier of the sheet is `1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY`, and the associated TXT record is:  ``` gods    120 IN  TXT \"sheet=1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY\" ```  #### script  You can automatically insert a custom JavaScript file in the login.html, consent.html, and test.html pages. The URL of this file can be specified in the `script` parameter. By inserting a custom JavaScript file, you can also integrate a client-side random user generator.  #### summary  You can provide a short, one-line description, a watchword for the tenant in the `summary` parameter. It appears on the tenant's startup page and all the pages that contain a list of available tenants.  #### about  To provide a detailed description of the tenant, use the `about` parameter. If it takes the value of a URL, the description is downloaded from the given URL; otherwise the value is the description itself. The description may have markdown formatting.  #### attribution  It is an external data source. If you use a random user generator, you can specify the attribution in the `attribution` parameter. The attribution may have markdown formatting, that is, you can highlight any element or provide a link to an external source:  ``` randomuser  120 IN  TXT \"attribution=User data generated using [RANDOM USER GENERATOR](https://randomuser.me/).\" ```  #### logo  It is the URL of the tenant's logo. The image at this address appears in the address bar of the tenant's webpages.  #### favicon  Use the `favicon` parameter to provide the URL of the favicon. The image at this address appears as a shortcut icon in the browser when a user visits the tenant's webpages.  ### Examples  PhantAuth offers several examples for creating a custom tenant. They are ready-to-use tenants, although primarily created to show examples for customization.  #### faker  A [PhantAuth Faker](https://phantauth.net/_faker) tenant contains a generator built on the JavaScript Faker library. The generator runs on the serverless deployment platform of [ZEIT Now](https://now.sh), available free of charge. Its source code is accessible in the [phantauth-faker](https://github.com/phantauth/phantauth-faker) GitHub repository. Its DNS configuration is:  ``` faker.phantauth.net. 120    IN  TXT \"factories=team\" faker.phantauth.net. 120    IN  TXT \"factories=user\" faker.phantauth.net. 120    IN  TXT \"flags=small\" faker.phantauth.net. 120    IN  TXT \"factory=https://phantauth-faker.now.sh/api{/kind,name}\" faker.phantauth.net. 120    IN  TXT \"userinfo=Dream Team\" faker.phantauth.net. 120    IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/united/bootstrap.min.css\" faker.phantauth.net. 120    IN  TXT \"logo=https://phantauth-faker.now.sh/faker-logo.svg\" faker.phantauth.net. 120    IN  TXT \"name=PhantAuth Faker\" ```  #### chance  A [PhantAuth Chance](https://phantauth.net/_chance) tenant contains a generator built on the JavaScript Chance library. The generator runs on the serverless deployment platform of [ZEIT Now](https://now.sh), available free of charge. Its source code is accessible in the [phantauth-chance](https://github.com/phantauth/phantauth-chance) GitHub repository. Its DNS configuration is:  ``` chance.phantauth.net. 120   IN  TXT \"flags=small\" chance.phantauth.net. 120   IN  TXT \"name=PhantAuth Chance\" chance.phantauth.net. 120   IN  TXT \"factory=https://phantauth-chance.now.sh/api{/kind,name}\" chance.phantauth.net. 120   IN  TXT \"factories=team\" chance.phantauth.net. 120   IN  TXT \"factories=user\" chance.phantauth.net. 120   IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/united/bootstrap.min.css\" chance.phantauth.net. 120   IN  TXT \"logo=https://phantauth-chance.now.sh/chance-logo.png\" ```  #### casual  A [PhantAuth Casual](https://phantauth.net/_casual) tenant contains a generator built on the JavaScript Casual library. The generator runs on the serverless deployment platform of [Auth0 Webtask](https://webtask.io), available free of charge. Its source code is accessible in the [phantauth-casual](https://github.com/phantauth/phantauth-casual) GitHub repository. Its DNS configuration is:  ``` casual.phantauth.net. 120   IN  TXT \"logo=https://www.phantauth.net/logo/phantauth-logo-gray.svg\" casual.phantauth.net. 120   IN  TXT \"name=PhantAuth Casual\" casual.phantauth.net. 120   IN  TXT \"factory=https://wt-51217f7b3eee6aead0123eeafe3b83e8-0.sandbox.auth0-extend.com/user{?name}\" casual.phantauth.net. 120   IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" ```  #### gods  For the [Greek Gods](https://phantauth.net/_gods) tenant, the user data is contained in a [public Google Sheets](https://docs.google.com/spreadsheets/d/1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY/) document. Its DNS configuration is:  ``` gods.phantauth.net. 120 IN  TXT \"attribution=God pictures come from  [Theoi Project](https://www.theoi.com/), a site exploring Greek mythology and the gods in classical literature and art.\" gods.phantauth.net. 120 IN  TXT \"name=Greek Gods\" gods.phantauth.net. 120 IN  TXT \"flags=medium\" gods.phantauth.net. 120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/sandstone/bootstrap.min.css\" gods.phantauth.net. 120 IN  TXT \"logo=https://cdn.staticaly.com/favicons/www.theoi.com\" gods.phantauth.net. 120 IN  TXT \"sheet=1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY\" ```  #### randomuser  The [RANDOM USER](https://phantauth.net/_randomuser) tenant uses the popular https://randomuser.me service to generate random users. The randomuser.me service is called on the client side, the call is contained in the [randomuser.js](https://www.phantauth.net/selfie/randomuser.js) script given in the `script` parameter. Its DNS configuration is:  ``` randomuser.phantauth.net.   120 IN  TXT \"attribution=User data generated using [RANDOM USER GENERATOR](https://randomuser.me/).\" randomuser.phantauth.net.   120 IN  TXT \"script=https://www.phantauth.net/selfie/randomuser.js\" randomuser.phantauth.net.   120 IN  TXT \"flags=small\" randomuser.phantauth.net.   120 IN  TXT \"name=RANDOM USER\" randomuser.phantauth.net.   120 IN  TXT \"logo=https://cdn.staticaly.com/favicons/randomuser.me\" randomuser.phantauth.net.   120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/sandstone/bootstrap.min.css\" ```  #### uinames  The [uinames](https://phantauth.net/_uinames) tenant uses the https://uinames.com service to generate random users. The uinames.com service is called on the client side, the call is contained in the [uinames.js](https://www.phantauth.net/selfie/uinames.js) script given in the `script` parameter. Its DNS configuration is:  ``` uinames.phantauth.net.  120 IN  TXT \"attribution=User data generated using [uinames.com API](https://uinames.com).\" uinames.phantauth.net.  120 IN  TXT \"logo=https://uinames.com/assets/img/ios-precomposed.png\" uinames.phantauth.net.  120 IN  TXT \"flags=small\" uinames.phantauth.net.  120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/minty/bootstrap.min.css\" uinames.phantauth.net.  120 IN  TXT \"name=uinames\" uinames.phantauth.net.  120 IN  TXT \"script=https://www.phantauth.net/selfie/uinames.js\" ```  #### mockaroo  The [Mockaroo](https://phantauth.net/_mockaroo) tenant uses the https://mockaroo.com service to generate random users. The mockaroo.com service is called on the client side, the call is contained in the [mockaroo.js](https://www.phantauth.net/selfie/mockaroo.js) script given in the `script` parameter. Its DNS configuration is:  ``` mockaroo.phantauth.net. 120 IN  TXT \"attribution=User data generated using [Mockaroo's Mock APIs](https://mockaroo.com/mock_apis).\" mockaroo.phantauth.net. 120 IN  TXT \"script=https://www.phantauth.net/selfie/mockaroo.js\" mockaroo.phantauth.net. 120 IN  TXT \"logo=https://www.phantauth.net/selfie/kongaroo.svg\" mockaroo.phantauth.net. 120 IN  TXT \"flags=small\" mockaroo.phantauth.net. 120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/minty/bootstrap.min.css\" mockaroo.phantauth.net. 120 IN  TXT \"name=Mockaroo\" ```  ## Pricing  PhantAuth is a free, open-source, non-profit application. If you find this service useful and can afford, please make a small donation as a contribution to the operation costs (domain registration, service hosting, etc.)  [Donate on Ko-fi](https://ko-fi.com/Q5Q0T7C7) | [Donate on Liberapay](https://liberapay.com/szkiba/donate) | [Donate on PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=VXLCJ3EZRAE7G&source=url)  ## Generator  The basic concept of PhantAuth is that it generates data in a random but deterministic way. To achieve this goal, a so-called pseudorandom number generator (PRNG) is used. Each object type has an identifier (login name for user, client_id for client, etc.) By using a given hash algorithm, the value of the pseudorandom generator seed is produced from this identifier. Then, every property of the given object is generated with the pseudorandom generator started from this seed value. Taking advantage of the special feature of the pseudorandom number generator, also called as deterministic random bit generator (DRBG), that is, it generates the same random value series started from the same seed, the identifier clearly defines the object generated from it. That is, by the use of an identifier and generator, you can regenarate the properties of a given object at any time.  Based on the above concept, PhantAuth is absolutely stateless, and no storage medium is necessary. So, a randomly selected login name will \"exist\", and the properties of the \"associated\" user can be generated.  ### Identifier  In brief, an object is defined by its identifier. The name of the identifier of a user or client object is `sub` or `client_id` used in the OpenID Connect specifications. The name of the identifier property of other PhantAuth-specific objects that are not included in the specifications is `sub`.  The identifier may contain any character.  ### Customization  Sometimes you may want to customize the properties generated from the identifier. Although the identifier may contain any character, and its structure is optional, you can customize the generated values if a certain structure is used.  #### Flags  You can use a variety of flags to customize or give the parameters of certain object properties (user, client, etc.). The flags can be grouped by their effect on the generation of the properties. Basically, a flag is a keyword. You can set more than one flags to affect the generation of a variety of properties at the same time. To separate the flags from one another and the rest of the identifier, you need to use a semicolon `;`:  ``` joe;female;kitten ```  In the above example, the user generated by the user generator is female, and her avatar is a randomly selected sketched kitten avatar. The other features are deterministically generated from the name \"joe\", that is, their values are not affected by the two flags. The [profile page](https://phantauth.net/%7Ejoe%3bfemale%3bkitten) of this example can be found [here](https://phantauth.net/%7Ejoe%3bfemale%3bkitten).  Please note that the flags form part of the identifier, as a different flag allows you to generate a different object.  ##### User gender flags  The following flags modify the gender of the generated user.  Flag | Description --- | --- male | The `gender` property of the generated user is male, independent of the user's name female | The `gender` property of the generated user is female, independent of the user's name guess | The `gender` property is defined on the basis of the generated user's given name (default) nogender | The generated user doesn't have a `gender` property  ##### User avatar flags  The following flags modify the generated avatar image.  Avatar | Flag | Description --- | --- | --- ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQCAwMDAgQDAwMEBAQEBQkGBQUFBQsICAYJDQsNDQ0LDAwOEBQRDg8TDwwMEhgSExUWFxcXDhEZGxkWGhQWFxb/2wBDAQQEBAUFBQoGBgoWDwwPFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhb/wgARCAAgACADAREAAhEBAxEB/8QAGAAAAwEBAAAAAAAAAAAAAAAABQcIBgT/xAAZAQACAwEAAAAAAAAAAAAAAAACBQEDBAb/2gAMAwEAAhADEAAAAC6Xe29GzHjM+gFAVhqJajyCeLlrIXbWPewzZijGPPvG/NwoetBt08tMkn//xAAqEAABBAEDAwMDBQAAAAAAAAABAgMEBREABhIHITETIkEIFWEjMlFxof/aAAgBAQABPwDoBVvmxe3DuSZCnJjKxAaaaBSlwYJcJz8ZSB+VDVjQ3Ni+L+ukOh9LRaS1IkFCSknvhKchJyB/IOB21vOduKNt+TC3LspNpVvHhKWC26koPYqcb4+5I+SSSPOrjpbVN2D1bt+ImJEkMpDjshCXHsqySGjjKRxKR7jnIOuhUaMxtlguVqY7rbi2kxArJCXMcV4wAByB8Z8E6n9TaSv3Wjbv2+zmPuKS0XWWx6SV+AknlkHP41Y9SqSbuqZtX7baR5rZWxzdY/RWvuCnkVd/6A8d9b86uWjd1Pq9gbUfdlR3lx3LFTBOVpUQotj9oTnwfONdEdwsU0lFHcwr+NYT3S5BVYyUSBz9MFaUnlyCQhkrHYgYWdXG762DdoW/ErgtlHMvynkMKkZ8IZUrty+T+AE5Gci26m1CGLO+broZQ0y9JcLcptx2MpIK1IdKSQOXwO5GoHVSss7kzbWqkyovqKWquE/0m3CpWTlSEBXgkY/0+Da9L7fY/wBUNYuXbxp1TupiwjUCe6HIkhtv1g0sEcQVMtuoCwdX93XVT8ytvYMkpT7WltoQpaUgkcClYOCDkeDqvsdoXcKTAuSKiisIsiqYfslAqlzZDZaQhtKQSSjklftHtJSdVzEqC7IiTWiw/FcWy6kkHgtJwpJI7ZBBGc41/8QAJREAAgIABQIHAAAAAAAAAAAAAQIAEQMEEjFBIVEFEyIycYHB/9oACAECAQE/AMsFY6wKqM/WxDiudhNbXqPEyTgYTKxsi4XrrvFY77QgM2omhMNhiMShBrtMJgxvtPc6qOYnhgVvU9/VfsbKocu2FhKF+O8S1NHoZkcvqfzX42nM/8QAIhEAAgICAgICAwAAAAAAAAAAAQIAEQMhBDESIhNBBTJx/9oACAEDAQE/ALLHcXB600PEXxu4cSeOonFyL4mtE9/yLjJNHUyLQI7FQkra9kTj8la+I/e9wJ61ZsxwqYmLH9RG5pK0q0Zg5ATMrt0DFfVg2J+W5nr8SffcB1P/2Q==) | ai | [AI](https://thispersondoesnotexist.com/) type generated, photo-like avatars (default) ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABelBMVEX////uuIw6TFomLDQ4SljuuYovQ1Hvuo5KMSztuI4xRFIxQ1DsuY3storvuY3+///zvY8nLTLc4ePx17zvxqPzvpP2wZHvuYrVpnyjfVycdlw1SFcyRlWWc1QjN0YqOEMoLDVMMCxILipFKyb6/Pv9/vn3+Pju8vPu8PDo6+337d/Bxcets7eHkZn1wZXotYrutonsuYiViobQonj7///79+/28unx4M3y2cbx3MO3v8Ozq6nov5ruvpLktYvxuIfpt4bbqYCnlIDQo33MoHlxdXmEd3O+k3C5kGqlgGA7TVueeVltXFktP0p2VURrTD0qNDsmMTgoLjIfJS8iKC1DMyX9/vvl6evq6Of28OHb1djb1NjEycvGwr/Jwb+yub3Cu7nu0rjt0bi3sazfvp7evZzpvJPdtZN+ipPpvJKdko/uvIx1gYrisIVxfIXRonqJe3pWZXGCb2iuhWRDU1+dd11pV1SGZE6BYU4tQE5iT0pXQkFDLylBKSPfP9FbAAABsklEQVQ4y62SV1fCMBhAm5C0tLWlIFOGAoqAAgLuvfdW3Hvvvcd/NynnCJLy5n3p+XJv25y03D+zttOV+Zy+qC2jNz6+w6FgMGjeNPbb4aA5T3jPyNeGQm9VhOfHWXM4wnpL19erA1AqhNnQoYUt7uacIB9UOOcyHMv0GFE0EEU8NmoQvFyqjqQAgOBwqNdGwYNz3ONxY+z2eMadmWbGt/T2ZDUNEwQt23PawgSVLqBOTNFXTE2oAFcaBWBoGBCGh4BR0JGmsimVaqLXdAcT1O0rRCjZW4UGB+z3Wmmlt2rJpEaOKt1qYZ/AdfcB4M/l/AD0dZORJd4vioLfL4hif5wzpE0RscuFRaWNK0P8RAVAPV/nytF87B4YcB9ZynmbzU5P0m6zGdloAgXq7fR3sNcHUCJa6hu8kATtCsZKezSAIGr46zt9EPL8SGww1TsYG+F5CKXOYr9KPJSkhWXT0pJpeUGSyOiLFW32hiwgXppfrCEszks8IgtXBR+R9YCvtpoI1mr+PXGGoBwp3iFBKgS++ycIvVu/QSOigVeeMenMyPqMdkuCSVnWvVWWJ/WgkbofGhc3SydvBmYAAAAASUVORK5CYII=) | sketch | sketched photo-like [avataaars](https://getavataaars.com/) avatars ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQDAwMDAgQDAwMEBAQFBgoGBgUFBgwICQcKDgwPDg4MDQ0PERYTDxAVEQ0NExoTFRcYGRkZDxIbHRsYHRYYGRj/2wBDAQQEBAYFBgsGBgsYEA0QGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBj/wgARCAAgACADAREAAhEBAxEB/8QAGAAAAwEBAAAAAAAAAAAAAAAABAcIBgP/xAAZAQEAAwEBAAAAAAAAAAAAAAAFAwQGAAH/2gAMAwEAAhADEAAAAKqCXmKa6P3Ur6dnoLS3qPAoU9InlVzAmWDq+q42gRzMJepNsBxZvCPWhP8A/8QALRAAAQQBAwMCAwkAAAAAAAAAAQIDBBEFAAYSByExE0EUFVEWIiMyQmFxkbH/2gAIAQEAAT8A+bIwOSlTA20iGpbzrzjaAXClKeXbt3rW8989V944c5+LGcfxU0r9CKy4GwGQriApI48/BNm71sHq71E2dPZjZfGvyMGshDsSSeaRyIFIJFJJ1Kw70zIJf2rFfeZUn8RvtTS+xKeRP0I89voT7TszHm4lczmlh1cFL7bJPZRWSKH8CzoTcpBlYrbLO3XlwxFQgzw4kJQoJF/cq6v31Ekqy3zLETNvS47ENbZTIk0W1lDyDYoX7WD5/bT+2mZ60oRkIhkFRWFsZN5pZUfJtKQfP11kus2zoKMWJ+OkyBFYZbRKQsUhSKBUgBXe/NEdxpzqTPlNujb8JhbuNQiPKTOfS1wVVd0+SCBYI1M6m42BDbi7i4QMpIPNccH1BxokKtN0OVV58HWG3jh1vw3JOIeeiLbDhkR5iSSon8vZsitSp7z7LranFEA3V/2f919stvbnxrOcTuc7czDjKGsi36XqJf4CgSixzr9JBujRB1ms+5kt2TJ6JcmQ2FhDbsmgtaU0ORA7C6Jr2urNXrozuCa9siZF+NcQwyQQk0QVEAEkHz4Tr//EACURAAICAQMCBwEAAAAAAAAAAAECAAMRBBIhMlEFExUiMUFxsf/aAAgBAgEBPwCtsEmeaith4GR+kxQzdIyJYhryByBLCQeJpF2glp6U46WENG4nJ+ZYWW7b9TSA2kl4umA9xPH7NvaHR2iwo67lzwe2ZVUKkCAYxPFw6otinAGf5xP/xAAgEQACAQUAAgMAAAAAAAAAAAABAgADBBESIQUxFSJx/9oACAEDAQE/AGTYCUbIlcr7lezKjMLhOMcGWxFZlU82MtlGvTL8FgFp+zifJUx7WCi66lTggyxVKqAM2DPIbp9KOCex3dTow7+Q1jgiU7ykUFVX1bHRHuGZ2cnMtwrkhhk8n//Z) | photo | photo avatars ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAASFBMVEX///AoHCf/4LXP1Yz////EzHL/3K3Tmob/5sRURUXWuppMNzoKBgnWz8Df0rhXhIg+NC0uIyrf5+jz9eTf2cr44sHZ15VMPj4HhT4EAAAAlElEQVQ4y72S2w6CMBBEpYhstRXx+v9/Ko4LS1sgmRfOQzPZOWnSy2FHqgxW8FVJ0vfT+Aw+Q/LL+zvgsy2sVW6BFFyvtRGCCRgcf7gskkJnQncvBZGriBvjSxJhlfSYNreLIoScTaFtOQF4rcDSl3lGzC4AMUb2T4ITQGSFdw2ax/COTf1n3ms9ogorQNGlFBI44QtzCgcBd0pFOQAAAABJRU5ErkJggg==) | dice | pixel art-style [DiceBear](https://github.com/DiceBear/avatars) avatars ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQCAwMDAgQDAwMEBAQEBQkGBQUFBQsICAYJDQsNDQ0LDAwOEBQRDg8TDwwMEhgSExUWFxcXDhEZGxkWGhQWFxb/2wBDAQQEBAUFBQoGBgoWDwwPFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhb/wgARCAAgACADAREAAhEBAxEB/8QAGQAAAgMBAAAAAAAAAAAAAAAABAYDBQgH/8QAGwEAAgMAAwAAAAAAAAAAAAAABQYBAwQAAgf/2gAMAwEAAhADEAAAANaJeOCqOd+iDnkJur0WoZYGhWcmLanlnJDCsyquYXZ9NWmmUpTHqfadDPhj/8QAKhAAAgICAQMDAwQDAAAAAAAAAQIDBAUREgAGIQciMRMVQSNCUXEyUmH/2gAIAQEAAT8Az3cdmbvpoqlmdqsE8dOKGFggaYuY3ck6J0zlNbA2m/J11lO985i+9rmOatHchV2P0nKxmFdnhpvnRXRPtY+V8aPXcnrtnKdmCnat0KkwTlYjhgkeSJ0mMb71vanTsnjzwAIcHz6HeoWb7zyUMZ4S0oIXWWyYDE9kr+8qQvBgSgKga9zHWtazNRZ8pnpnhlcUpLVmIQ+11lW0oVw2wVADOSR5A2RsgDpObF5XkeWSV2klkk1ykdjssQAACT+AAB8AADXSxVIu5ESDEsbeQhkaS5DVGiIyihJZB52eY4qd7CN/r1grAjz1evjK9iI1L1YN9CLgk6mdecaP/idPHp1HkFdEeR01atW9V7ONvQI9TMVXVY2GwxcBzv8AsxTf9G16z3Y9jHRvPQngejChZhM4jaFAP51xIA/JK6A+D1QTKXpoExKvWtyv+k0yKVQ+dc15r4PwAGB2QD/B9P8AsrK0cn937lyy3bKbaKCCNUhjZiWL6ABJ2ToHlrQPJm2x9R8NYvUosljQfuOOb6kPEbLgENrX5IKhgD86K/uJ67m7myncMfAwT16qIA1KA8nsOB7ixHll3sKh0NeXGzpOxe4Z4IMPnM/WnipySWK9yNNgpKkwVCfOw6hGP9+NAkdROskYdGBVgCpHwQev/8QALhEAAQMCBAMGBwEAAAAAAAAAAQIDEQQhAAUxgRJBURMUYXGRoQYQIiMzscHR/9oACAECAQE/AH83WM1TSoEpsDHXn6C2KrPHqOodS4ApIVAGhiAdb9eY3wxldPVNU9U09DawCQdTIsARoZsbcjjM+NjOVUrY+3w8XOb6e8jxicNMTXVrhMFMwehJ12/WKh9x91TrhlRwFvushHaEpSRCZOpm6RtfzGMuVVU1c32hMrIBBmYkfvQHzw22lnOXUKH0uoncWP8ATiu+FlcRXTrEdFct/wDcUFK49VBtogqGhmPQx/MUOUlp7vFQeJYsNbbmPYAXNtIzOkcdQl1j8jZkePUb4zTO6irUKanBSDY9Z5jyGMqR3SrVKZTYT0tNt42+X//EACwRAAIBAwEFBgcAAAAAAAAAAAECAwAEIRESMUFR8AWBkbHB0RATFBUyQqH/2gAIAQMBAT8Ae5P1IiFS3RhJ1znTTuHGvus+pATrrNWF286ja3jf78s0iazTNxFSOzsWbfQUspIPLHHNWu3FKuv7eNKoW6bkw8qm7OJJKN4+9QRFpNlT/dPT0qK22W2239dbhU8ZcBl/Jcj276ubt5D8tMc6t0EUxxjHl8P/2Q==) | kitten | [ROBOHASH](https://robohash.org/)-generated sketched kitten avatars ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAcFBQYFBAcGBQYIBwcIChELCgkJChUPEAwRGBUaGRgVGBcbHichGx0lHRcYIi4iJSgpKywrGiAvMy8qMicqKyr/2wBDAQcICAoJChQLCxQqHBgcKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKir/wgARCAAgACADAREAAhEBAxEB/8QAGQAAAgMBAAAAAAAAAAAAAAAAAAUDBAYB/8QAGgEBAAMAAwAAAAAAAAAAAAAAAAIDBAEFBv/aAAwDAQACEAMQAAAAc9Z7oAAFM8lXmOgr25uzDMTxt5Ku5DQgtxWBpXr/AP/EACgQAAICAQMDBAEFAAAAAAAAAAECAwQRBRIhAAYxEBMiUQdBRXFzwv/aAAgBAQABPwD0BBzgg444Prc1F1p+7PQtiNZzkIoYlEG7ewPhcjwfOP1z1oGqi7BLLQRrETXNkkjZVtpiQiTHOcnB8+Gz6d394J2tQSdKZuu03tOqvsEZ2hvk2DgkHjqHvLQZHENm/WqzGNHMU0yHAZQw+QJU8H7/AJA6m7p0CooD6rTHgKkcgY/QAA603uGC/repaU0FivZoOqSrPGF5OfjkE/Lg8HB6s6VTutKbMCSrNGI5UcZSRQcjcp4JHOD5H31N+Ne1p/2wJ/VLIP8AR6bsPQZ5o5b0E99oo1ijNy1JJsReFQZbhQOAPA6qaJp9F4zSqpXSLJjiiG2NWIwX2jy2ONxyccdf/8QAHxEAAgIBBAMAAAAAAAAAAAAAAQIAAxEQITFBEhMg/9oACAECAQE/APlRgxxvvpWnmYamXqCtj1GrKDJgYjie54bnMLluZ//EACgRAAEEAQICCwAAAAAAAAAAAAECAwQRACExBUEQEhUgIlFhgZGhwf/aAAgBAwEBPwDuvLK26o1f0OeR12klOuv5v0SpYjpsCzdY1OYcTqqj66YqUwgWVjI8tD6ilPLFsocvrDfOzY/kfnE8NjjcE++Nx22z4BWf/9k=) | adorable | [Adorable Avatars](http://avatars.adorable.io/) ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQCAwMDAgQDAwMEBAQEBQkGBQUFBQsICAYJDQsNDQ0LDAwOEBQRDg8TDwwMEhgSExUWFxcXDhEZGxkWGhQWFxb/2wBDAQQEBAUFBQoGBgoWDwwPFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhb/wgARCAAgACADAREAAhEBAxEB/8QAGgAAAgIDAAAAAAAAAAAAAAAAAAcBBAIGCP/EABQBAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAOii6BSAb5InzIaoCqNqGQAtz//EACcQAAIBAwMCBgMAAAAAAAAAAAECAwQFEQAGQRKRBxAhMTJxE1HB/9oACAEBAAE/ANWe03G6OVoKV5un5N6BR9k4GrvaLlayBX0jxBvichlP0Rkeey4IYNrUKQABXgV2I5Zhlj3Ot4wQVG165JwCqwM4J4ZRkHuPKFHllWONCzuQqhRkkn2A1sS2XG12YQV06vn1SIDP4s+46udb4ttwudmanoKgJy8RGDLj1A6uP7+9So8UrxyIVdCVYMMEEe4OvCOgSpvc1ZIARSRjoB4ZsgHsG8/FqgSmvcVZGABVxnrA5ZcAnsV1/8QAFBEBAAAAAAAAAAAAAAAAAAAAQP/aAAgBAgEBPwAH/8QAFBEBAAAAAAAAAAAAAAAAAAAAQP/aAAgBAwEBPwAH/9k=) | mp | simple, cartoon-style silhouetted outline of a person (does not vary by user) ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVPMTn///+hkZWsnqKWhInz8fG3q67o5OVjymXqAAAAoElEQVQoz82OwQ3CMBAEV8ENXCzxdjowHeBHCnBQ/jRB/2TWwjVwq5H2tXOK3HPkLYAoaq9RlwCirNeFNnCqyoUWcM7jcxQpwX7upzdWqcHciJIC5kasLcAb+DVudPwaNzp+pOBO5S1wx6/HXeCOX7e3wN3+caPbP879b/4oetoPSt447Ac1b/SCFFJ4o6/4ocXYsB9+G/bD3MAPcwM/kC/KhCQv+Oa0WgAAAABJRU5ErkJggg==) | identicon | a geometric pattern based on an email hash ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAB2lBMVEXw3/Q3t350dHTn1+uwo7LAssOnp6dVVVWhoaGamprs3PDp2e3j0+ZxcXHZyt2UlJQ1sXlwcHBcW1zTxNapnauMjIyHfol3b3lvb29qampoZ2jh0eTez+K5ubmmm6iakJyYj5qTiZV+mJOSkpKIh4h8fHx4eHg0p3RsbGxiYGJQUFAgbUvQwdPOwNLNzc3Hucq/vcC5rbu4q7u2qrmVjJeWlpaTk5ORh5OPiZGPj4+LhoxylouJgYuAd4JzioB+dYB+fH96eHs0rXcwoW9uZ29Chmg7hWVkY2VgW2I4c1lOTU9MTEzJu8y9r8C0p7e1tbWyqbWiqa+rn66ro62qqqqkmKahl6Ock56MnJyFgYWEhIR1hn98c35lf3ZzbnRJhmsvmGlUdmg4jGctkmVkXWVRaV9fX180eltEa1kmf1dFZVdVUVZHR0f////o2OzVytvY2NjT0tPKvs3AvMjCtMXCu8Sqsbeor7WxsbGtobCurq6mqqicn6ajo6Oenp6OjZWJiYlymohwj4dxioVDt4Nil4N4i4OAgIAzqXQ6onRcfm85mW5LgWw6kWtkbGhgaGdAgWRUbGMwimJNZF5KZFxZWVlLVFBJRUo9UEg5UEgfZ0c8PDw7OTsgQzTXmnPvAAACSUlEQVQ4y42ShXPiQBSH325ISBqCe4sWKFJ3B4pD3d2u3p67u7v7/3pLgB5Q5ua+yWQy+X37due9hf9CXl/1z/zC+XPjZyBHK4BGVi6Mn+64EV0Wi1BWoCahnJrmxmaZLKinAKrpKykeQDIDwE9ZLoNItWGgiQe+YWCZgpaJOvT47OSwPGhINjY3ips1qf0Zv3qErx81bMHVCEJoUxvVO7p+9VxrgSyrWIqPjF59FdADH+tIXhcIPOxP4CO11waEUR8RjH6887VL/mo/gFDkxxBCKfxZKsXeWSJsYSwVH+Hta4TW9yMBRFDuZXAGY5MWIGne8Ru9RNgm5QlkuWgcYJMaq3xWANA4ZrRp6fYzVMK6GadxkpZDHvoUKmNX9TOhKRpH34Nve8fShy+/+zbUvn4oYc6UKghx2/Vsh6lSoSp6QLLYS/Lqg4rUfFduLlluPkJovuKlGLF+ejc9uHSfVLgrOxE3HAq17O7gEyXK8ibca6OLT0C1uxnF01Dn2BoS2WAZhgvrG46b4GLYWmFsZS2uzAkxXQfHkn+5ccoWdIxCZ5oeJGmBF5yC5Wo7JWL5MMfc4ViVJY7+MvS+e5HrIVeAUN/TybDu7pAlhop4fpE3L87lDqgyGiSUJuRxrzid8xKRW07nBCzcloBIt8IB0Mq4OC0UI8O6vDB7D1MAU71WvkSQuIz5TjTpFG1wkvYOoTCkVXclwaXozec2qVmtLY81/WnhsEb8NJhUgkdwlObVCZXZ4/ENA+ESTbfa7V1lAk23tdvtQQr+AEpRWa/mX8zUAAAAAElFTkSuQmCC) | monsterid | a generated \"monster\" with different colors, faces, etc. ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQDAwMDAgQDAwMEBAQFBgoGBgUFBgwICQcKDgwPDg4MDQ0PERYTDxAVEQ0NExoTFRcYGRkZDxIbHRsYHRYYGRj/2wBDAQQEBAYFBgsGBgsYEA0QGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBj/wgARCAAgACADAREAAhEBAxEB/8QAGwAAAQQDAAAAAAAAAAAAAAAABAMFBgcBAgj/xAAbAQACAwEBAQAAAAAAAAAAAAACAwAEBgcBBf/aAAwDAQACEAMQAAAA7bDwNf1URYFK7aFah061OMmdYZHaxjHR6yMLmEsbVQ8o1RuMQhGZD//EAC4QAAEDAwMBBwIHAAAAAAAAAAECAwQFESEABhIHEyIxUVKR0kGiFSMkNGFiof/aAAgBAQABPwD8Vlvy0R4pbF0laluXISBbFhbxv5/TTm4JLTpQZcXH9VfLTm55KGlLEqKbD0K+WqDvw1Sqv054Nh1CO0Spu4BSDYggk+ac3zc4Fs06euQ6+Uryhk/6U63HRRL620eGjY8KpUidBck1iryePNiV3vygmwNgUoAJKuQXcHGOn9I/QVmpVzaEbblbiVYx6ezG4FMmJ61FKbpAGQoqss4462nNVG3u6ortyiuj729bOqTbzs/tFjDIt76mVVbFUkJehurY5XQ+xZfdsLhSb8r8uXgCLWzpdWXI4oiwng0T33n7NpCfrZJPMny7oH86jTRG3chSVYVHeH3tapPV52lKfLRbd7ZHCy74ze+DpXWCSpfK8T2V8tHq7IN/2nsr5af6lokPNPHsm1tIUm7dxfkQT4k+lOv/xAAiEQACAgECBwEAAAAAAAAAAAABAgARAwQSEyExQWGBwfD/2gAIAQIBAT8A3Q5wIdQBMOoGW67QtamZCoQFW5xypw3u5/u00Brf6+wMNpuEi+sYius0Zrf6+zjCiDKTzKTzEdUFLP/EADARAAECBAIGCQUAAAAAAAAAAAIBEQADBSEEBgciMUFhkRITVGKSwcLS4UJRcoGh/9oACAEDAQE/AJA9Y99kDSTJHRV5fMDRTJWf+fMValzKb0FNXQnbdsZ7ftIoKocwkXh5xgJc6ZiSGfL1b/TZtyou/nGFHEDUEFJbBd9WyJ+W/nGkRhDCt3vTGVnmTDbh5xLA0HZaJYH0ktGkzVDCP3/TGX81FSJxTEBDQkuiq2zjeE0vn2UfEvthNMB9lHxL7YzPnebXylqYIAi7IivtZ72+0f/Z) | wavatar | generated faces with varying features and backgrounds ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAABlBMVEVLAmn9LdWXmTS+AAAAMUlEQVQI12N4wMDAj0wUyCATDAUyDMgE/wMEARbDIOQbmD8gEx/kkQmZApkCJIIwAAAZjxw4Pi/EJgAAAABJRU5ErkJggg==) | retro | awesome generated, 8-bit arcade-style pixelated faces ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wgARCAAgACADAREAAhEBAxEB/8QAGgAAAQUBAAAAAAAAAAAAAAAACQABBgcIBP/EABkBAAIDAQAAAAAAAAAAAAAAAAAFAwQGAf/aAAwDAQACEAMQAAAAKmFTQT2dNB19GAcj3fTwWbgRZRgG/Z38htKyALMogqCxfyBdakdVZv8A/8QAKBAAAQMDBAEEAgMAAAAAAAAAAgEDBAUGEQAHCBIhEBMiMRQkMkJS/9oACAEBAAE/ANbv71SdsatRILFtzqutSkjH98U6MopKiIiH5yXlVxj+uqe6+9BYclMDGkmCE4yLnuIBY8j2wmcfWcevNTlQtyXJKsq3ak/T4dEnKD8qKRNGclvIkvuf5RVIRQcYUVJV1wb5PXJet1zbBvGpFWjKN+ZSqm8Qm9gfJsmafz+OSQl+SYJF9d+OJNfi7n3XV27br9xU2rVBZ8OTQBjGgA453eB4XF7IY5JBwnVdcCuOVXS8I+69RzTKE2zJYosJ0wKU+hEbSuPIHxFBHI4+1L15N7k1javbF2r0IYS1A5Tcb94FMUAhMjUQQh7lgPrKa4b7/wC4q3jaVty3YMbbFme9RTMWA7rLfZekMNqXZXEVTEkFcIOkXOv/xAAlEQABAwEIAgMAAAAAAAAAAAABAgMEEQAFEBITITFBMlFCccH/2gAIAQIBAT8Ast0INKWHG+MJiMkZ5XfA/bXjDbaGqz4+sZN43olDTd2aSQkHNqBRJPxpl6913s/eDsiO227TOAMxGwJ7oPVeK4xmkvOpbUaV2tNitQyW6kq6+sP/xAAkEQABAwQBAwUAAAAAAAAAAAABAgMRAAQFIRASMXETFEFRof/aAAgBAwEBPwCm2usEzXjnCYfqb9w62VSNa1FZjGt249dgQmYI5x+Xtk26G3DBSIOu+jG/MTWWyiLlsMt7+z2/ObFlFw+lpwwDWSsbeyBbBJX8eOP/2Q==) | robohash | a generated robot with different colors, faces, etc. ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAAA1BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAAtJREFUCNdjGOQAAACgAAH4BzM6AAAAAElFTkSuQmCC) | blank | a transparent PNG image   | notfound | return an HTTP 404 (File Not Found) response   | noavatar | the user will not have a `picture` property  ##### Client logo flags  The following flags modify the generated logo.  Logo | Flag | Description --- | --- | --- ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAJFBMVEX/VyL76ef+dkz71s774t39noL8uqf9kXD+glz/Zjb8xrf9qZHgm7oqAAAAlElEQVQoz6XNwQ0CMQwEwPUhIZ5rgcQXRAOUcCUcJVACHVACdEAJlMh5E5Dlzz1YR4k0iWN4yQ9WFWALQPgSWAYgALh1wBxa7E/BC5jAIyICAHbmbhNgM7Dd6GTAA5HTXa5KuVSwsQL/Bx8rqCowfbG1Agzw3HENmNAzODwWU4fA04wG7A/eJviKHeCCJsMea29Q8gH9RxXZMd8OgAAAAABJRU5ErkJggg==) | icon | [Game-icons.net](https://game-icons.net/) icon as a logo (default) ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBAUEBAYFBQUGBgYHCQ4JCQgICRINDQoOFRIWFhUSFBQXGiEcFxgfGRQUHScdHyIjJSUlFhwpLCgkKyEkJST/2wBDAQYGBgkICREJCREkGBQYJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCT/wgARCAAgACADAREAAhEBAxEB/8QAGQAAAwADAAAAAAAAAAAAAAAAAwQGAgUH/8QAGAEBAQEBAQAAAAAAAAAAAAAABgUEAwL/2gAMAwEAAhADEAAAAASHNXa056c8HP8ANkeusPyLOLuuNvc5byaaDbHQy6XH2GuA1ZxYPrmmEZP/xAAuEAABAwIFAwIEBwAAAAAAAAABAgMEBREAITFBUQYScQciFGGBoRMyM4KRksH/2gAIAQEAAT8A9HPT1mndMtPSWEKkPgPvFY3Oif2jFIpIlTZbIUoMpUlBUDmfbfI83++KlCXSHwxEJSJC9ASeVKt87ZeABtj1YoEiu0B2LNYR8THBehu6kLAuW720UBa17XANztSOokwaOSMwoFSlk2CTve+nP1x03W2GWnXJDqWUuO5FZ7ArPM57knTxpiqVVpVUgFVz2lRBPix+x+xx1xKjSobamFBStAUkHOxIz8gHBpyZcj8U+1squv3WCc/GoJH8njOJGbkLKVuraQpAUhIV+Ygg9pO4NsxwPGKhAkxgiK4opfjICw4q/cogDjQk2H1POH5lReaWmSsPFA7UWCQCom225sc+LnI3t05UY/UNFiVRkBRdQEvI07XAlQWP7km3BBxGmOxYJi/DtusKIUF6qQf9Gmp2xUJTD6OyO4p1Q/UWSVdxyyGW1uecdTTo9Ao8uovaMBYabXY9zujQA+V0g22F8f/EACwRAAECBQICCgMAAAAAAAAAAAECBAADESExEkEFYRMUMlFxkcHh8PEigdH/2gAIAQIBAT8A4k5UFdCnAz4+0NXC1MES0mn5H+w0dFpImrVemK3vT6MNn6nZKJhqoYhwhap9KXMM2iGzWWiYoAm+dztztHHmpS11p2Vf9j2hlMMtwlQ2IhHCZ8qdrVhO+ceQMO19aWrWvSUdkd45czmGM2aUKaTb6sD09YZcJWp2lGkgA38AeflCp5nNqitabZsKYia0UhJHbBNlYp31r8pCGhTN6RJ1KF1KJsOX0IW4UJSp69sV54PzIBMf/8QAKxEAAgECBAQFBQEAAAAAAAAAAQIRAAMEBSExE0FRYRIicYHBMlKRodHw/9oACAEDAQE/AMutjA4dfvfU9ulYu4i3uKwBaNPzRspi2Qt3n0msyyyy+HLWOWtXcKtxg5MAVnPFu32aypIUAbToOf73rIvExdWO66ex1rBWHCOj9Kv51hnAVWktsJ117bilThongSZPm7aTPxWIawFGKtkQDqff+0+Y20wzXZBkae9ZeFW8HYjXrMT0nl27GKwuJ494XSeGyyGT6vFGxEH4NHHlbbC6ptqfKiBRJjn6eugoJwXKqYG8Dr0P+MSB1j//2Q==) | fractal | [Electric Sheep](https://electricsheep.org/) fractal as a logo  ##### `Group` size flags  The following flag modify the sizes of the generated team (group of users) and fleet (group of clients).  Flag | Size --- | --- tiny | 5 (default) small | 10 medium | 25 large | 50 huge | 100  #### Name  In most cases, the generated objects have a full name, which is generated from the identifier. Instead of being generated, the full name can be produced from the identifier, if the identifier contains at least one period (`.`) or space (` `) character. In such cases, these characters play the role of separator between the parts of the full name (e.g. family name, given name). That is, the full name isn't randomly generated from the identifier but, by taking the separator characters into account,  it is produced from the single parts of the full name (with capitalised initial letters). For this purpose, it is advised to use a period character, rather than a space character.  ``` joe.black;sketch ```  In the above example: The full name of the user generated by the user generator is *Joe Black* (and his avatar is a skecthed profile avatar). The [profile page](https://phantauth.net/%7Ejoe.black%3bsketch) of this example can be found [here](https://phantauth.net/%7Ejoe.black%3bsketch).  #### Picture  In most cases, the generated objects have an image (avatar for a user, logo for a client), which is generated from the identifier. The *flags* determine which pre-defined inventory the image comes from (see [flags](#flags)). It can be further customized by the use of [Gravatar](https://gravatar.com).  Each object has a generated unique email address (`email` for a user, `logo_email` for any other objects). To customize the image of a given object, you need to assign the gravatar image to this email address. By default, an object has a gravatar image, and the generated image is the default value of the gravatar URL only. In other words, as soon as you create a gravatar image to a given email address, that image will appear as the image associated with the given object.  #### Email  A disposable, operational email address suitable for receiving incoming emails is generated to each object. You can use your own email address (e.g. a previously set test email address) instead of a generated email address, if you prefer. In this case, the identifier contains an email address. Consequently, the image associated with the given object is the gravatar image assigned to the email address contained in the identifier.  ``` ivan.test.szkiba@spam4.me ```  In the above example: The email address of the user generated by the user generator is *ivan.test.szkiba@spam4.me* (and his name is *Ivan Test Szkiba*). The [profile page](https://phantauth.net/%7Eivan.test.szkiba%40spam4.me) of this example can be found [here](https://phantauth.net/%7Eivan.test.szkiba%40spam4.me).  ### Custom Generators  PhantAuth can use external data sources and generators as well. The only restriction is that the external generator has to be deterministic. This means that even if called several times, it has to generate the same object to the same identifier.  A special case of external generators is if an external data source is used. In such cases, the properties of a given object can be provided in a comma separated value (CSV) file or a Google Sheets document.  The external data sources and generators can be defined by the use of so-called [tenants](https://doc.phantauth.net/#/tenant). To learn more, please go to chapter [Tenant](https://doc.phantauth.net/#/tenant).
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import okhttp3.*;
import okhttp3.internal.http.HttpMethod;
import okhttp3.internal.tls.OkHostnameVerifier;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import okio.Buffer;
import okio.BufferedSink;
import okio.Okio;

import javax.net.ssl.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Type;
import java.net.URI;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.openapitools.client.auth.Authentication;
import org.openapitools.client.auth.HttpBasicAuth;
import org.openapitools.client.auth.HttpBearerAuth;
import org.openapitools.client.auth.ApiKeyAuth;

/**
 * <p>ApiClient class.</p>
 */
public class ApiClient {

    private String basePath = "https://phantauth.net";
    protected List<ServerConfiguration> servers = new ArrayList<ServerConfiguration>(Arrays.asList(
    new ServerConfiguration(
      "https://phantauth.net",
      "No description provided",
      new HashMap<String, ServerVariable>()
    )
  ));
    protected Integer serverIndex = 0;
    protected Map<String, String> serverVariables = null;
    private boolean debugging = false;
    private Map<String, String> defaultHeaderMap = new HashMap<String, String>();
    private Map<String, String> defaultCookieMap = new HashMap<String, String>();
    private String tempFolderPath = null;

    private Map<String, Authentication> authentications;

    private DateFormat dateFormat;
    private DateFormat datetimeFormat;
    private boolean lenientDatetimeFormat;
    private int dateLength;

    private InputStream sslCaCert;
    private boolean verifyingSsl;
    private KeyManager[] keyManagers;

    private OkHttpClient httpClient;
    private JSON json;

    private HttpLoggingInterceptor loggingInterceptor;

    /**
     * Basic constructor for ApiClient
     */
    public ApiClient() {
        init();
        initHttpClient();

        // Setup authentications (key: authentication name, value: authentication).
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Basic constructor with custom OkHttpClient
     *
     * @param client a {@link okhttp3.OkHttpClient} object
     */
    public ApiClient(OkHttpClient client) {
        init();

        httpClient = client;

        // Setup authentications (key: authentication name, value: authentication).
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    private void initHttpClient() {
        initHttpClient(Collections.<Interceptor>emptyList());
    }

    private void initHttpClient(List<Interceptor> interceptors) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.addNetworkInterceptor(getProgressInterceptor());
        for (Interceptor interceptor: interceptors) {
            builder.addInterceptor(interceptor);
        }

        httpClient = builder.build();
    }

    private void init() {
        verifyingSsl = true;

        json = new JSON();

        // Set default User-Agent.
        setUserAgent("OpenAPI-Generator/1.0.0/java");

        authentications = new HashMap<String, Authentication>();
    }

    /**
     * Get base path
     *
     * @return Base path
     */
    public String getBasePath() {
        return basePath;
    }

    /**
     * Set base path
     *
     * @param basePath Base path of the URL (e.g https://phantauth.net
     * @return An instance of OkHttpClient
     */
    public ApiClient setBasePath(String basePath) {
        this.basePath = basePath;
        this.serverIndex = null;
        return this;
    }

    public List<ServerConfiguration> getServers() {
        return servers;
    }

    public ApiClient setServers(List<ServerConfiguration> servers) {
        this.servers = servers;
        return this;
    }

    public Integer getServerIndex() {
        return serverIndex;
    }

    public ApiClient setServerIndex(Integer serverIndex) {
        this.serverIndex = serverIndex;
        return this;
    }

    public Map<String, String> getServerVariables() {
        return serverVariables;
    }

    public ApiClient setServerVariables(Map<String, String> serverVariables) {
        this.serverVariables = serverVariables;
        return this;
    }

    /**
     * Get HTTP client
     *
     * @return An instance of OkHttpClient
     */
    public OkHttpClient getHttpClient() {
        return httpClient;
    }

    /**
     * Set HTTP client, which must never be null.
     *
     * @param newHttpClient An instance of OkHttpClient
     * @return Api Client
     * @throws java.lang.NullPointerException when newHttpClient is null
     */
    public ApiClient setHttpClient(OkHttpClient newHttpClient) {
        this.httpClient = Objects.requireNonNull(newHttpClient, "HttpClient must not be null!");
        return this;
    }

    /**
     * Get JSON
     *
     * @return JSON object
     */
    public JSON getJSON() {
        return json;
    }

    /**
     * Set JSON
     *
     * @param json JSON object
     * @return Api client
     */
    public ApiClient setJSON(JSON json) {
        this.json = json;
        return this;
    }

    /**
     * True if isVerifyingSsl flag is on
     *
     * @return True if isVerifySsl flag is on
     */
    public boolean isVerifyingSsl() {
        return verifyingSsl;
    }

    /**
     * Configure whether to verify certificate and hostname when making https requests.
     * Default to true.
     * NOTE: Do NOT set to false in production code, otherwise you would face multiple types of cryptographic attacks.
     *
     * @param verifyingSsl True to verify TLS/SSL connection
     * @return ApiClient
     */
    public ApiClient setVerifyingSsl(boolean verifyingSsl) {
        this.verifyingSsl = verifyingSsl;
        applySslSettings();
        return this;
    }

    /**
     * Get SSL CA cert.
     *
     * @return Input stream to the SSL CA cert
     */
    public InputStream getSslCaCert() {
        return sslCaCert;
    }

    /**
     * Configure the CA certificate to be trusted when making https requests.
     * Use null to reset to default.
     *
     * @param sslCaCert input stream for SSL CA cert
     * @return ApiClient
     */
    public ApiClient setSslCaCert(InputStream sslCaCert) {
        this.sslCaCert = sslCaCert;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>keyManagers</code>.</p>
     *
     * @return an array of {@link javax.net.ssl.KeyManager} objects
     */
    public KeyManager[] getKeyManagers() {
        return keyManagers;
    }

    /**
     * Configure client keys to use for authorization in an SSL session.
     * Use null to reset to default.
     *
     * @param managers The KeyManagers to use
     * @return ApiClient
     */
    public ApiClient setKeyManagers(KeyManager[] managers) {
        this.keyManagers = managers;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>dateFormat</code>.</p>
     *
     * @return a {@link java.text.DateFormat} object
     */
    public DateFormat getDateFormat() {
        return dateFormat;
    }

    /**
     * <p>Setter for the field <code>dateFormat</code>.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setDateFormat(DateFormat dateFormat) {
        JSON.setDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set SqlDateFormat.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setSqlDateFormat(DateFormat dateFormat) {
        JSON.setSqlDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set OffsetDateTimeFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        JSON.setOffsetDateTimeFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LocalDateFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLocalDateFormat(DateTimeFormatter dateFormat) {
        JSON.setLocalDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LenientOnJson.</p>
     *
     * @param lenientOnJson a boolean
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLenientOnJson(boolean lenientOnJson) {
        JSON.setLenientOnJson(lenientOnJson);
        return this;
    }

    /**
     * Get authentications (key: authentication name, value: authentication).
     *
     * @return Map of authentication objects
     */
    public Map<String, Authentication> getAuthentications() {
        return authentications;
    }

    /**
     * Get authentication for the given name.
     *
     * @param authName The authentication name
     * @return The authentication, null if not found
     */
    public Authentication getAuthentication(String authName) {
        return authentications.get(authName);
    }


    /**
     * Helper method to set username for the first HTTP basic authentication.
     *
     * @param username Username
     */
    public void setUsername(String username) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setUsername(username);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set password for the first HTTP basic authentication.
     *
     * @param password Password
     */
    public void setPassword(String password) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setPassword(password);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set API key value for the first API key authentication.
     *
     * @param apiKey API key
     */
    public void setApiKey(String apiKey) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKey(apiKey);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set API key prefix for the first API key authentication.
     *
     * @param apiKeyPrefix API key prefix
     */
    public void setApiKeyPrefix(String apiKeyPrefix) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKeyPrefix(apiKeyPrefix);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set access token for the first OAuth2 authentication.
     *
     * @param accessToken Access token
     */
    public void setAccessToken(String accessToken) {
        throw new RuntimeException("No OAuth2 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param sessionToken Session Token
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String sessionToken, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Set the User-Agent header's value (by adding to the default header map).
     *
     * @param userAgent HTTP request's user agent
     * @return ApiClient
     */
    public ApiClient setUserAgent(String userAgent) {
        addDefaultHeader("User-Agent", userAgent);
        return this;
    }

    /**
     * Add a default header.
     *
     * @param key The header's key
     * @param value The header's value
     * @return ApiClient
     */
    public ApiClient addDefaultHeader(String key, String value) {
        defaultHeaderMap.put(key, value);
        return this;
    }

    /**
     * Add a default cookie.
     *
     * @param key The cookie's key
     * @param value The cookie's value
     * @return ApiClient
     */
    public ApiClient addDefaultCookie(String key, String value) {
        defaultCookieMap.put(key, value);
        return this;
    }

    /**
     * Check that whether debugging is enabled for this API client.
     *
     * @return True if debugging is enabled, false otherwise.
     */
    public boolean isDebugging() {
        return debugging;
    }

    /**
     * Enable/disable debugging for this API client.
     *
     * @param debugging To enable (true) or disable (false) debugging
     * @return ApiClient
     */
    public ApiClient setDebugging(boolean debugging) {
        if (debugging != this.debugging) {
            if (debugging) {
                loggingInterceptor = new HttpLoggingInterceptor();
                loggingInterceptor.setLevel(Level.BODY);
                httpClient = httpClient.newBuilder().addInterceptor(loggingInterceptor).build();
            } else {
                final OkHttpClient.Builder builder = httpClient.newBuilder();
                builder.interceptors().remove(loggingInterceptor);
                httpClient = builder.build();
                loggingInterceptor = null;
            }
        }
        this.debugging = debugging;
        return this;
    }

    /**
     * The path of temporary folder used to store downloaded files from endpoints
     * with file response. The default value is <code>null</code>, i.e. using
     * the system's default temporary folder.
     *
     * @see <a href="https://docs.oracle.com/javase/7/docs/api/java/nio/file/Files.html#createTempFile(java.lang.String,%20java.lang.String,%20java.nio.file.attribute.FileAttribute...)">createTempFile</a>
     * @return Temporary folder path
     */
    public String getTempFolderPath() {
        return tempFolderPath;
    }

    /**
     * Set the temporary folder path (for downloading files)
     *
     * @param tempFolderPath Temporary folder path
     * @return ApiClient
     */
    public ApiClient setTempFolderPath(String tempFolderPath) {
        this.tempFolderPath = tempFolderPath;
        return this;
    }

    /**
     * Get connection timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getConnectTimeout() {
        return httpClient.connectTimeoutMillis();
    }

    /**
     * Sets the connect timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param connectionTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setConnectTimeout(int connectionTimeout) {
        httpClient = httpClient.newBuilder().connectTimeout(connectionTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get read timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getReadTimeout() {
        return httpClient.readTimeoutMillis();
    }

    /**
     * Sets the read timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param readTimeout read timeout in milliseconds
     * @return Api client
     */
    public ApiClient setReadTimeout(int readTimeout) {
        httpClient = httpClient.newBuilder().readTimeout(readTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get write timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getWriteTimeout() {
        return httpClient.writeTimeoutMillis();
    }

    /**
     * Sets the write timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param writeTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setWriteTimeout(int writeTimeout) {
        httpClient = httpClient.newBuilder().writeTimeout(writeTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }


    /**
     * Format the given parameter object into string.
     *
     * @param param Parameter
     * @return String representation of the parameter
     */
    public String parameterToString(Object param) {
        if (param == null) {
            return "";
        } else if (param instanceof Date || param instanceof OffsetDateTime || param instanceof LocalDate) {
            //Serialize to json string and remove the " enclosing characters
            String jsonStr = JSON.serialize(param);
            return jsonStr.substring(1, jsonStr.length() - 1);
        } else if (param instanceof Collection) {
            StringBuilder b = new StringBuilder();
            for (Object o : (Collection) param) {
                if (b.length() > 0) {
                    b.append(",");
                }
                b.append(o);
            }
            return b.toString();
        } else {
            return String.valueOf(param);
        }
    }

    /**
     * Formats the specified query parameter to a list containing a single {@code Pair} object.
     *
     * Note that {@code value} must not be a collection.
     *
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list containing a single {@code Pair} object.
     */
    public List<Pair> parameterToPair(String name, Object value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value instanceof Collection) {
            return params;
        }

        params.add(new Pair(name, parameterToString(value)));
        return params;
    }

    /**
     * Formats the specified collection query parameters to a list of {@code Pair} objects.
     *
     * Note that the values of each of the returned Pair objects are percent-encoded.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list of {@code Pair} objects.
     */
    public List<Pair> parameterToPairs(String collectionFormat, String name, Collection value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value.isEmpty()) {
            return params;
        }

        // create the params based on the collection format
        if ("multi".equals(collectionFormat)) {
            for (Object item : value) {
                params.add(new Pair(name, escapeString(parameterToString(item))));
            }
            return params;
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        // escape all delimiters except commas, which are URI reserved
        // characters
        if ("ssv".equals(collectionFormat)) {
            delimiter = escapeString(" ");
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = escapeString("\t");
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = escapeString("|");
        }

        StringBuilder sb = new StringBuilder();
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(escapeString(parameterToString(item)));
        }

        params.add(new Pair(name, sb.substring(delimiter.length())));

        return params;
    }

    /**
    * Formats the specified free-form query parameters to a list of {@code Pair} objects.
    *
    * @param value The free-form query parameters.
    * @return A list of {@code Pair} objects.
    */
    public List<Pair> freeFormParameterToPairs(Object value) {
        List<Pair> params = new ArrayList<>();

        // preconditions
        if (value == null || !(value instanceof Map )) {
            return params;
        }

        final Map<String, Object> valuesMap = (Map<String, Object>) value;

        for (Map.Entry<String, Object> entry : valuesMap.entrySet()) {
            params.add(new Pair(entry.getKey(), parameterToString(entry.getValue())));
        }

        return params;
    }


    /**
     * Formats the specified collection path parameter to a string value.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param value The value of the parameter.
     * @return String representation of the parameter
     */
    public String collectionPathParameterToString(String collectionFormat, Collection value) {
        // create the value based on the collection format
        if ("multi".equals(collectionFormat)) {
            // not valid for path params
            return parameterToString(value);
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        if ("ssv".equals(collectionFormat)) {
            delimiter = " ";
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = "\t";
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = "|";
        }

        StringBuilder sb = new StringBuilder() ;
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(parameterToString(item));
        }

        return sb.substring(delimiter.length());
    }

    /**
     * Sanitize filename by removing path.
     * e.g. ../../sun.gif becomes sun.gif
     *
     * @param filename The filename to be sanitized
     * @return The sanitized filename
     */
    public String sanitizeFilename(String filename) {
        return filename.replaceAll(".*[/\\\\]", "");
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * "* / *" is also default to JSON
     * @param mime MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    public boolean isJsonMime(String mime) {
        String jsonMime = "(?i)^(application/json|[^;/ \t]+/[^;/ \t]+[+]json)[ \t]*(;.*)?$";
        return mime != null && (mime.matches(jsonMime) || mime.equals("*/*"));
    }

    /**
     * Select the Accept header's value from the given accepts array:
     *   if JSON exists in the given array, use it;
     *   otherwise use all of them (joining into a string)
     *
     * @param accepts The accepts array to select from
     * @return The Accept header to use. If the given array is empty,
     *   null will be returned (not to set the Accept header explicitly).
     */
    public String selectHeaderAccept(String[] accepts) {
        if (accepts.length == 0) {
            return null;
        }
        for (String accept : accepts) {
            if (isJsonMime(accept)) {
                return accept;
            }
        }
        return StringUtil.join(accepts, ",");
    }

    /**
     * Select the Content-Type header's value from the given array:
     *   if JSON exists in the given array, use it;
     *   otherwise use the first one of the array.
     *
     * @param contentTypes The Content-Type array to select from
     * @return The Content-Type header to use. If the given array is empty,
     *   returns null. If it matches "any", JSON will be used.
     */
    public String selectHeaderContentType(String[] contentTypes) {
        if (contentTypes.length == 0) {
            return null;
        }

        if (contentTypes[0].equals("*/*")) {
            return "application/json";
        }

        for (String contentType : contentTypes) {
            if (isJsonMime(contentType)) {
                return contentType;
            }
        }

        return contentTypes[0];
    }

    /**
     * Escape the given string to be used as URL query value.
     *
     * @param str String to be escaped
     * @return Escaped string
     */
    public String escapeString(String str) {
        try {
            return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
        } catch (UnsupportedEncodingException e) {
            return str;
        }
    }

    /**
     * Deserialize response body to Java object, according to the return type and
     * the Content-Type response header.
     *
     * @param <T> Type
     * @param response HTTP response
     * @param returnType The type of the Java object
     * @return The deserialized Java object
     * @throws org.openapitools.client.ApiException If fail to deserialize response body, i.e. cannot read response body
     *   or the Content-Type of the response is not supported.
     */
    @SuppressWarnings("unchecked")
    public <T> T deserialize(Response response, Type returnType) throws ApiException {
        if (response == null || returnType == null) {
            return null;
        }

        if ("byte[]".equals(returnType.toString())) {
            // Handle binary response (byte array).
            try {
                return (T) response.body().bytes();
            } catch (IOException e) {
                throw new ApiException(e);
            }
        } else if (returnType.equals(File.class)) {
            // Handle file downloading.
            return (T) downloadFileFromResponse(response);
        }

        String respBody;
        try {
            if (response.body() != null)
                respBody = response.body().string();
            else
                respBody = null;
        } catch (IOException e) {
            throw new ApiException(e);
        }

        if (respBody == null || "".equals(respBody)) {
            return null;
        }

        String contentType = response.headers().get("Content-Type");
        if (contentType == null) {
            // ensuring a default content type
            contentType = "application/json";
        }
        if (isJsonMime(contentType)) {
            return JSON.deserialize(respBody, returnType);
        } else if (returnType.equals(String.class)) {
            // Expecting string, return the raw response body.
            return (T) respBody;
        } else {
            throw new ApiException(
                    "Content type \"" + contentType + "\" is not supported for type: " + returnType,
                    response.code(),
                    response.headers().toMultimap(),
                    respBody);
        }
    }

    /**
     * Serialize the given Java object into request body according to the object's
     * class and the request Content-Type.
     *
     * @param obj The Java object
     * @param contentType The request Content-Type
     * @return The serialized request body
     * @throws org.openapitools.client.ApiException If fail to serialize the given object
     */
    public RequestBody serialize(Object obj, String contentType) throws ApiException {
        if (obj instanceof byte[]) {
            // Binary (byte array) body parameter support.
            return RequestBody.create((byte[]) obj, MediaType.parse(contentType));
        } else if (obj instanceof File) {
            // File body parameter support.
            return RequestBody.create((File) obj, MediaType.parse(contentType));
        } else if ("text/plain".equals(contentType) && obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else if (isJsonMime(contentType)) {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            return RequestBody.create(content, MediaType.parse(contentType));
        } else if (obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else {
            throw new ApiException("Content type \"" + contentType + "\" is not supported");
        }
    }

    /**
     * Download file from the given response.
     *
     * @param response An instance of the Response object
     * @throws org.openapitools.client.ApiException If fail to read file content from response and write to disk
     * @return Downloaded file
     */
    public File downloadFileFromResponse(Response response) throws ApiException {
        try {
            File file = prepareDownloadFile(response);
            BufferedSink sink = Okio.buffer(Okio.sink(file));
            sink.writeAll(response.body().source());
            sink.close();
            return file;
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * Prepare file for download
     *
     * @param response An instance of the Response object
     * @return Prepared file for the download
     * @throws java.io.IOException If fail to prepare file for download
     */
    public File prepareDownloadFile(Response response) throws IOException {
        String filename = null;
        String contentDisposition = response.header("Content-Disposition");
        if (contentDisposition != null && !"".equals(contentDisposition)) {
            // Get filename from the Content-Disposition header.
            Pattern pattern = Pattern.compile("filename=['\"]?([^'\"\\s]+)['\"]?");
            Matcher matcher = pattern.matcher(contentDisposition);
            if (matcher.find()) {
                filename = sanitizeFilename(matcher.group(1));
            }
        }

        String prefix = null;
        String suffix = null;
        if (filename == null) {
            prefix = "download-";
            suffix = "";
        } else {
            int pos = filename.lastIndexOf(".");
            if (pos == -1) {
                prefix = filename + "-";
            } else {
                prefix = filename.substring(0, pos) + "-";
                suffix = filename.substring(pos);
            }
            // Files.createTempFile requires the prefix to be at least three characters long
            if (prefix.length() < 3)
                prefix = "download-";
        }

        if (tempFolderPath == null)
            return Files.createTempFile(prefix, suffix).toFile();
        else
            return Files.createTempFile(Paths.get(tempFolderPath), prefix, suffix).toFile();
    }

    /**
     * {@link #execute(Call, Type)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @return ApiResponse&lt;T&gt;
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call) throws ApiException {
        return execute(call, null);
    }

    /**
     * Execute HTTP call and deserialize the HTTP response body into the given return type.
     *
     * @param returnType The return type used to deserialize HTTP response body
     * @param <T> The return type corresponding to (same with) returnType
     * @param call Call
     * @return ApiResponse object containing response status, headers and
     *   data, which is a Java object deserialized from response body and would be null
     *   when returnType is null.
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call, Type returnType) throws ApiException {
        try {
            Response response = call.execute();
            T data = handleResponse(response, returnType);
            return new ApiResponse<T>(response.code(), response.headers().toMultimap(), data);
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * {@link #executeAsync(Call, Type, ApiCallback)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @param callback ApiCallback&lt;T&gt;
     */
    public <T> void executeAsync(Call call, ApiCallback<T> callback) {
        executeAsync(call, null, callback);
    }

    /**
     * Execute HTTP call asynchronously.
     *
     * @param <T> Type
     * @param call The callback to be executed when the API call finishes
     * @param returnType Return type
     * @param callback ApiCallback
     * @see #execute(Call, Type)
     */
    @SuppressWarnings("unchecked")
    public <T> void executeAsync(Call call, final Type returnType, final ApiCallback<T> callback) {
        call.enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                callback.onFailure(new ApiException(e), 0, null);
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                T result;
                try {
                    result = (T) handleResponse(response, returnType);
                } catch (ApiException e) {
                    callback.onFailure(e, response.code(), response.headers().toMultimap());
                    return;
                } catch (Exception e) {
                    callback.onFailure(new ApiException(e), response.code(), response.headers().toMultimap());
                    return;
                }
                callback.onSuccess(result, response.code(), response.headers().toMultimap());
            }
        });
    }

    /**
     * Handle the given response, return the deserialized object when the response is successful.
     *
     * @param <T> Type
     * @param response Response
     * @param returnType Return type
     * @return Type
     * @throws org.openapitools.client.ApiException If the response has an unsuccessful status code or
     *                      fail to deserialize the response body
     */
    public <T> T handleResponse(Response response, Type returnType) throws ApiException {
        if (response.isSuccessful()) {
            if (returnType == null || response.code() == 204) {
                // returning null if the returnType is not defined,
                // or the status code is 204 (No Content)
                if (response.body() != null) {
                    try {
                        response.body().close();
                    } catch (Exception e) {
                        throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                    }
                }
                return null;
            } else {
                return deserialize(response, returnType);
            }
        } else {
            String respBody = null;
            if (response.body() != null) {
                try {
                    respBody = response.body().string();
                } catch (IOException e) {
                    throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                }
            }
            throw new ApiException(response.message(), response.code(), response.headers().toMultimap(), respBody);
        }
    }

    /**
     * Build HTTP call with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP call
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Call buildCall(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        Request request = buildRequest(baseUrl, path, method, queryParams, collectionQueryParams, body, headerParams, cookieParams, formParams, authNames, callback);

        return httpClient.newCall(request);
    }

    /**
     * Build an HTTP request with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP request
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Request buildRequest(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        final String url = buildUrl(baseUrl, path, queryParams, collectionQueryParams);

        // prepare HTTP request body
        RequestBody reqBody;
        String contentType = headerParams.get("Content-Type");
        String contentTypePure = contentType;
        if (contentTypePure != null && contentTypePure.contains(";")) {
            contentTypePure = contentType.substring(0, contentType.indexOf(";"));
        }
        if (!HttpMethod.permitsRequestBody(method)) {
            reqBody = null;
        } else if ("application/x-www-form-urlencoded".equals(contentTypePure)) {
            reqBody = buildRequestBodyFormEncoding(formParams);
        } else if ("multipart/form-data".equals(contentTypePure)) {
            reqBody = buildRequestBodyMultipart(formParams);
        } else if (body == null) {
            if ("DELETE".equals(method)) {
                // allow calling DELETE without sending a request body
                reqBody = null;
            } else {
                // use an empty request body (for POST, PUT and PATCH)
                reqBody = RequestBody.create("", contentType == null ? null : MediaType.parse(contentType));
            }
        } else {
            reqBody = serialize(body, contentType);
        }

        List<Pair> updatedQueryParams = new ArrayList<>(queryParams);

        // update parameters with authentication settings
        updateParamsForAuth(authNames, updatedQueryParams, headerParams, cookieParams, requestBodyToString(reqBody), method, URI.create(url));

        final Request.Builder reqBuilder = new Request.Builder().url(buildUrl(baseUrl, path, updatedQueryParams, collectionQueryParams));
        processHeaderParams(headerParams, reqBuilder);
        processCookieParams(cookieParams, reqBuilder);

        // Associate callback with request (if not null) so interceptor can
        // access it when creating ProgressResponseBody
        reqBuilder.tag(callback);

        Request request = null;

        if (callback != null && reqBody != null) {
            ProgressRequestBody progressRequestBody = new ProgressRequestBody(reqBody, callback);
            request = reqBuilder.method(method, progressRequestBody).build();
        } else {
            request = reqBuilder.method(method, reqBody).build();
        }

        return request;
    }

    /**
     * Build full URL by concatenating base path, the given sub path and query parameters.
     *
     * @param baseUrl The base URL
     * @param path The sub path
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @return The full URL
     */
    public String buildUrl(String baseUrl, String path, List<Pair> queryParams, List<Pair> collectionQueryParams) {
        final StringBuilder url = new StringBuilder();
        if (baseUrl != null) {
            url.append(baseUrl).append(path);
        } else {
            String baseURL;
            if (serverIndex != null) {
                if (serverIndex < 0 || serverIndex >= servers.size()) {
                    throw new ArrayIndexOutOfBoundsException(String.format(
                    "Invalid index %d when selecting the host settings. Must be less than %d", serverIndex, servers.size()
                    ));
                }
                baseURL = servers.get(serverIndex).URL(serverVariables);
            } else {
                baseURL = basePath;
            }
            url.append(baseURL).append(path);
        }

        if (queryParams != null && !queryParams.isEmpty()) {
            // support (constant) query string in `path`, e.g. "/posts?draft=1"
            String prefix = path.contains("?") ? "&" : "?";
            for (Pair param : queryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    url.append(escapeString(param.getName())).append("=").append(escapeString(value));
                }
            }
        }

        if (collectionQueryParams != null && !collectionQueryParams.isEmpty()) {
            String prefix = url.toString().contains("?") ? "&" : "?";
            for (Pair param : collectionQueryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    // collection query parameter value already escaped as part of parameterToPairs
                    url.append(escapeString(param.getName())).append("=").append(value);
                }
            }
        }

        return url.toString();
    }

    /**
     * Set header parameters to the request builder, including default headers.
     *
     * @param headerParams Header parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processHeaderParams(Map<String, String> headerParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : headerParams.entrySet()) {
            reqBuilder.header(param.getKey(), parameterToString(param.getValue()));
        }
        for (Entry<String, String> header : defaultHeaderMap.entrySet()) {
            if (!headerParams.containsKey(header.getKey())) {
                reqBuilder.header(header.getKey(), parameterToString(header.getValue()));
            }
        }
    }

    /**
     * Set cookie parameters to the request builder, including default cookies.
     *
     * @param cookieParams Cookie parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processCookieParams(Map<String, String> cookieParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : cookieParams.entrySet()) {
            reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
        }
        for (Entry<String, String> param : defaultCookieMap.entrySet()) {
            if (!cookieParams.containsKey(param.getKey())) {
                reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
            }
        }
    }

    /**
     * Update query and header parameters based on authentication settings.
     *
     * @param authNames The authentications to apply
     * @param queryParams List of query parameters
     * @param headerParams Map of header parameters
     * @param cookieParams Map of cookie parameters
     * @param payload HTTP request body
     * @param method HTTP method
     * @param uri URI
     * @throws org.openapitools.client.ApiException If fails to update the parameters
     */
    public void updateParamsForAuth(String[] authNames, List<Pair> queryParams, Map<String, String> headerParams,
                                    Map<String, String> cookieParams, String payload, String method, URI uri) throws ApiException {
        for (String authName : authNames) {
            Authentication auth = authentications.get(authName);
            if (auth == null) {
                throw new RuntimeException("Authentication undefined: " + authName);
            }
            auth.applyToParams(queryParams, headerParams, cookieParams, payload, method, uri);
        }
    }

    /**
     * Build a form-encoding request body with the given form parameters.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyFormEncoding(Map<String, Object> formParams) {
        okhttp3.FormBody.Builder formBuilder = new okhttp3.FormBody.Builder();
        for (Entry<String, Object> param : formParams.entrySet()) {
            formBuilder.add(param.getKey(), parameterToString(param.getValue()));
        }
        return formBuilder.build();
    }

    /**
     * Build a multipart (file uploading) request body with the given form parameters,
     * which could contain text fields and file fields.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyMultipart(Map<String, Object> formParams) {
        MultipartBody.Builder mpBuilder = new MultipartBody.Builder().setType(MultipartBody.FORM);
        for (Entry<String, Object> param : formParams.entrySet()) {
            if (param.getValue() instanceof File) {
                File file = (File) param.getValue();
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), file);
            } else if (param.getValue() instanceof List) {
                List list = (List) param.getValue();
                for (Object item: list) {
                    if (item instanceof File) {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), (File) item);
                    } else {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
                    }
                }
            } else {
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
            }
        }
        return mpBuilder.build();
    }

    /**
     * Guess Content-Type header from the given file (defaults to "application/octet-stream").
     *
     * @param file The given file
     * @return The guessed Content-Type
     */
    public String guessContentTypeFromFile(File file) {
        String contentType = URLConnection.guessContentTypeFromName(file.getName());
        if (contentType == null) {
            return "application/octet-stream";
        } else {
            return contentType;
        }
    }

    /**
     * Add a Content-Disposition Header for the given key and file to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder 
     * @param key The key of the Header element
     * @param file The file to add to the Header
     */ 
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, File file) {
        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"; filename=\"" + file.getName() + "\"");
        MediaType mediaType = MediaType.parse(guessContentTypeFromFile(file));
        mpBuilder.addPart(partHeaders, RequestBody.create(file, mediaType));
    }

    /**
     * Add a Content-Disposition Header for the given key and complex object to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder
     * @param key The key of the Header element
     * @param obj The complex object to add to the Header
     */
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, Object obj) {
        RequestBody requestBody;
        if (obj instanceof String) {
            requestBody = RequestBody.create((String) obj, MediaType.parse("text/plain"));
        } else {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            requestBody = RequestBody.create(content, MediaType.parse("application/json"));
        }

        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"");
        mpBuilder.addPart(partHeaders, requestBody);
    }

    /**
     * Get network interceptor to add it to the httpClient to track download progress for
     * async requests.
     */
    private Interceptor getProgressInterceptor() {
        return new Interceptor() {
            @Override
            public Response intercept(Interceptor.Chain chain) throws IOException {
                final Request request = chain.request();
                final Response originalResponse = chain.proceed(request);
                if (request.tag() instanceof ApiCallback) {
                    final ApiCallback callback = (ApiCallback) request.tag();
                    return originalResponse.newBuilder()
                        .body(new ProgressResponseBody(originalResponse.body(), callback))
                        .build();
                }
                return originalResponse;
            }
        };
    }

    /**
     * Apply SSL related settings to httpClient according to the current values of
     * verifyingSsl and sslCaCert.
     */
    private void applySslSettings() {
        try {
            TrustManager[] trustManagers;
            HostnameVerifier hostnameVerifier;
            if (!verifyingSsl) {
                trustManagers = new TrustManager[]{
                        new X509TrustManager() {
                            @Override
                            public void checkClientTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public void checkServerTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                                return new java.security.cert.X509Certificate[]{};
                            }
                        }
                };
                hostnameVerifier = new HostnameVerifier() {
                    @Override
                    public boolean verify(String hostname, SSLSession session) {
                        return true;
                    }
                };
            } else {
                TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());

                if (sslCaCert == null) {
                    trustManagerFactory.init((KeyStore) null);
                } else {
                    char[] password = null; // Any password will work.
                    CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
                    Collection<? extends Certificate> certificates = certificateFactory.generateCertificates(sslCaCert);
                    if (certificates.isEmpty()) {
                        throw new IllegalArgumentException("expected non-empty set of trusted certificates");
                    }
                    KeyStore caKeyStore = newEmptyKeyStore(password);
                    int index = 0;
                    for (Certificate certificate : certificates) {
                        String certificateAlias = "ca" + (index++);
                        caKeyStore.setCertificateEntry(certificateAlias, certificate);
                    }
                    trustManagerFactory.init(caKeyStore);
                }
                trustManagers = trustManagerFactory.getTrustManagers();
                hostnameVerifier = OkHostnameVerifier.INSTANCE;
            }

            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(keyManagers, trustManagers, new SecureRandom());
            httpClient = httpClient.newBuilder()
                            .sslSocketFactory(sslContext.getSocketFactory(), (X509TrustManager) trustManagers[0])
                            .hostnameVerifier(hostnameVerifier)
                            .build();
        } catch (GeneralSecurityException e) {
            throw new RuntimeException(e);
        }
    }

    private KeyStore newEmptyKeyStore(char[] password) throws GeneralSecurityException {
        try {
            KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            keyStore.load(null, password);
            return keyStore;
        } catch (IOException e) {
            throw new AssertionError(e);
        }
    }

    /**
     * Convert the HTTP request body to a string.
     *
     * @param requestBody The HTTP request object
     * @return The string representation of the HTTP request body
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object into a string
     */
    private String requestBodyToString(RequestBody requestBody) throws ApiException {
        if (requestBody != null) {
            try {
                final Buffer buffer = new Buffer();
                requestBody.writeTo(buffer);
                return buffer.readUtf8();
            } catch (final IOException e) {
                throw new ApiException(e);
            }
        }

        // empty http request body
        return "";
    }
}
