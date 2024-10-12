/**
 * PhantAuth
 * Random User Generator + OpenID Connect Provider. Like Lorem Ipsum, but for user accounts and authentication.  The PhantAuth API documentation is available on the following API documentation sites:  - [apiary](https://phantauth.docs.apiary.io) (primary source)  - [speca](https://speca.io/phantauth/phantauth)  - [PhantAuth Developer Portal](https://www.phantauth.net/api)  ### TL;DR  **PhantAuth was designed to simplify testing for applications using OpenID Connect authentication by making use of random generated users.**  endpoint  | address --------- | ------- issuer    | https://phantauth.net discovery | https://phantauth.net/.well-known/openid-configuration  credential    | value ------------- | ----- client_id     | test.client client_secret | UTBcWwt5  ## OpenID Connect  The OpenID Connect Provider of PhantAuth supports the flows listed in the OpenID Connect specifications (Hybrid, Implicit, Authorization Code), as well as the Resource Owner Password grant type, specified in the OAuth 2.0 specifications. PhantAuth as an OpenID Connect Provider can be integrated with a variety of web applications, mobil applications, and  backend applications. The integration can be either direct, as in the case of the OpenID Connect Provider, or through an authentication integration service, as in the case of Auth0 or Azure Active Directory B2C. To learn more, please go to chapter [Integration](https://doc.phantauth.net/#/integration).  Examples:  - [Direct OpenID Connect integration](https://www.phantauth.net/test/oidc)  - [Auth0 Social Connections integration](https://www.phantauth.net/test/auth0)  - [Azure Active Directory B2C integration](https://www.phantauth.net/test/azure)  ## Random User  The random user generator of PhantAuth can also be used separately, independent of the OpenID Connect Provider. You can generate an optional number of test users. In the knowledge of their user name, the data of the generated users can be regenerated at any time (OpenID Connect *sub* claim). The generated users have a unique, operational, disposable email address, a profile picture selected from one of the multiple pools of pictures, and the usual profile data. Custom email addresses and profile pictures may also be added. The random user generator of PhantAuth can be fully customized. Additionally, you can link an external generator to the application. For details,please go to chapter [Generator](https://doc.phantauth.net/#/generator).  Test pages:  - [Default Generator Test Page](https://phantauth.net/test/user) (embedded generator)  - [Greek Gods Generator Test Page](https://phantauth.net/_gods/test/user) (embedded generator working from a Google Sheet)  - [Faker Generator Test Page](https://phantauth.net/_faker/test/user) (external generator using Javascript Faker library)  - [Chance Generator Test Page](https://phantauth.net/_chance/test/user) (external generator using Javascript Chance library)  - [Casual Generator Test Page](https://phantauth.net/_casual/test/user) (external generator using Javascript Casual library)  - [Randomuser Generator Test Page](https://phantauth.net/_randomuser/test/user) (client side generator using https://randomuser.me)  - [uinames Generator Test Page](https://phantauth.net/_uinames/test/user) (client side generator using https://uinames.com)  - [Mockaroo Generator Test Page](https://phantauth.net/_mockaroo/test/user) (client side generator using https://mockaroo.com)  Every random generated user has a profile page, which contains their profile data in a simple one-page format.  Profile examples:  - [Random Profile](https://phantauth.net/%7Ejoe.black)  - [Random Greek God Profile](https://phantauth.net/_gods/%7Ezeus)  - [Random Faker Profile](https://phantauth.net/_faker/%7Eharry.houdini)  - [Random Chance Profile](https://phantauth.net/_chance/%7Epeter.pan)  - [Random Casual Profile](https://phantauth.net/_casual/%7Ejohn.smith)  ## CodeSandbox  The use of the random user generator and the direct integration of  the OpenID Connect is demonstrated through a set of CodeSandbox samples. The sample applications are run directly from CodeSandbox, so the source code is easy to view, edit, and test.  Examples:  - [Random User Generator usage exampe](https://4xyj8lw394.codesandbox.io/)  - [OpenID Connect direct integration exampe](https://8z77681269.codesandbox.io/)  ## Tenants  The PhantAuth is extremely versatile and customizable. You can use your own random user service, or generate users from an external .csv file or Google Sheet. You can use a set of Bootstrap themes to tailor the look and feel of the profile, morover, you can fundamentally change the same look and feel by the use of your own HTML templates. To find out more, please go to chapter [Tenant](https://doc.phantauth.net/#/tenant).  To customize the application, you need to use one or more so-called tenants. A tenant can be consiered as an independent PhantAuth service. A tenant has its own random user generator endpoints and OpenID Connect endpoints.  The tenants can be organised into so-called domains. Practically, a domain is a DNS zone, which contains the settings of the given tenant(s). The tenants as well as the domain can be configured by the use of DNS TXT records.  In addition to the default tenant, the PhantAuth domain contains some sample tenants, which are primarily designed to demonstrate customizability, a range of hosting possibilities, and the links to external services. In most cases, using the [default tenant](https://phantauth.net) is enough.  - [PhantAuth Default](https://phantauth.net) - default tenant, based on a Java Fairy library  - [Greek Gods](https://phantauth.net/_gods) - based on a Google Sheet document  - [PhantAuth Faker](https://phantauth.net/_faker) - based on a Javascript Faker library, hosted at https://now.sh  - [PhantAuth Chance](https://phantauth.net/_chance) - based on a Javascript Chance library, hosted at https://now.sh  - [PhantAuth Casual](https://phantauth.net/_casual) - based on a Javascript Casual library, hosted at https://webtask.io  - [RANDOM USER](https://phantauth.net/_randomuser) - based on https://randomuser.me service  - [uinames](https://phantauth.net/_uinames) - based on https://uinames.com service  - [Mockaroo](https://phantauth.net/_mockaroo) - based on  https://mockaroo.com service  Anyone can create a domain and the tenants. Sharing the tenants is facilitated by the [PhantAuth Shared Domain](https://shared.phantauth.net). A shared domain is connected to the [phantauth.cf](http://phantauth.cf) DNS zone, where anyone can create tenant configuration nodes by the use of the [FreeDNS](https://freedns.afraid.org/) service.  ### Concept  The internal structure of PhantAuth is modular enough to allow certain elements to be customized or even replaced. The customized PhantAuth instances can be considered as separate services, which are independent from the original one. For the sake of simplicity, the customized PhantAuth instances will be called **tenants**.  The customized PhantAuth instances (tenants) have a different URL from that of the default tenant. For technological and cloud hosting purposes, it is advised that only the beginning of the path component of these URLs differs from the default PhantAuth URL. Similarly, the path component of a tenant URL should start with a low line character (\"_\"). So the general format of a tenant URL is:  ``` https://phantauth.net/_TENANT ```  where `TENANT` is the name of the tenant. The tenant name is a DNS domain name at the same time, which may lack `.phantauth.net` or `.phantauth.cf` from the end.  ### DNS for configuration  When desiging PhantAuth, the aim is that PhantAuth can run without a database, and it is configurable by the users. This can be achieved if for the purpose of storing the tenant configuration, the system uses the special TXT records of the Domain Name System (DNS), in compliance with the [RFC 6763](https://tools.ietf.org/html/rfc6763) specifications. So the tenant name is one or more DNS TXT records. These TXT records contain the configuration properties in NAME=VALUE format.  This allows anyone to create their own tenants by creating a DNS domain and the TXT records in that domain. [Freenom](https://www.freenom.com), a service provider, allows you to register some top-level domains (.tk, .ml, .ga, .cf, .gq) free charge. The domain registered this way can be managed on the online interface of Freenom or transferred to an other free service provider offering a more convenient DNS name server (e.g. [CloudFlare](https://www.cloudflare.com/)). Additionally, [FreeDNS](https://freedns.afraid.org/) allows you to create DNS records within a second- or third level domain that is privately owned or shared with a community. In this case, you are advised to create the entries within the `phantauth.cf` domain, because here you can omit the `.phantauth.cf` from the tenant name in the URL. This means that a tenant with a name of `mytenant.phantauth.cf` can be referred to in the shorther `https://phantauth.net/_mytenant` format, rather than the longer `https://phantauth.net/_mytenant.phantauth.cf` URL . Similar to `.phantauth.cf`, the `phantauth.net` can be omitted, thus the officially supported and the example tenants can be referred to by their short names (e.g. https://phantauth.net/_faker).  In a nutshell, to create a tenant, you have the following options:  - With TXT records in a domain registered at Freenom, either on the online interface of Freenom or that of another free DNS service provider (e.g. CloudFlare).  - With TXT records created in a second- or third level domain shared with a community, by using FreeDNS.  - With TXT records created in your own existing DNS domain, by the use of an any DNS software.  ### Parameters  The below table contains a summary of the tenant parameters having an effect on the operation of the tenants.  Property | Description --- | --- [name](#name) | the displayed name of the tenant [flags](#flags) | generator flags having an effect on the login page [theme](#theme) | the address of the Bootstrap theme [template](#template) | the address of the HTML page templates [factory](#factory) | the address of the external user generator [depot](#depot) | the address of the external user database [sheet](#sheet) | the identifier of the Google Sheets document containing the user database [script](#script) | the JavaScript URL inserted in the HTML pages [summary](#summary) | a one-line summary of the tenant [about](#about) | a detailed description of the tenant [attribution](#attribution) | the specifications of the external source [logo](#logo) | the logo of the tenant [favicon](#favicon) | the favicon of the tenant's web pages  #### name  The displayed name of the tenant is defined in the `name` parameter. In lack of such a name, the tenant's DNS name is displayed. This name appears in the address bar of the tenant's webpages.  #### flags  This parameter contains the flags that affect the operation of a tenant (see [Flags](generator.md#flags)). Currently, the flags affecting the team size are used in the login screen. If any of the flags is a team size flag, you can select the user from a list in the login screen, rather than using an input field. It can take the following values:  - tiny  - small  - medium  - large  #### theme  The HTML page templates of a tenant are created by the use of the Bootstrap library. This allows you to customize the layout and the colours of the pages by using external Bootstrap CSS files. The `theme` parameter contains the URL of the Bootstrap CSS file used in the pages. It is optional; in lack of such a parameter, the tenant's HTML pages have the default layout provided in the [PhantAuth developer portal](https://www.phantauth.net).  #### template  The place of the HTML page templates of a tenant is specified by the `template` parameter. The value of the parameter is n [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) expression. The URI template receives the page name in a `resource` parameter.  The default value of the `template` parameter:  ``` https://default.phantauth.net{/resource} ```  The `resource` URI template parameter may take the following values:  Value | Description --- | --- tenant.html | the tenant's webpage; it contains a short description and the entry points of the tenant  user.html | the user's profile page login.html | the login page used for signing in consent.html | the content page used for signing in team.html | the profile page of the user group client.html | the profile page of a client fleet.html | the profile page of the client group policy.html | the client's privacy policy tos.html | a client's terms of service test.html | a login test page of the user generator and OpenID Connect  If you use your own template, the pages are fully customizable. The templates use a template engine called [Thymeleaf](https://www.thymeleaf.org/), which provides flexible template options. The source of the default template is available in the [phantauth-default](https://github.com/phantauth/phantauth-default) GitHub repository. If you wish to create your own templates, you are advised to produce them from these templates.  #### factory  PhantAuth allows you to use your own random resource (user, team) generator. To do so, you need to provide its address in the `factory` tenant parameter. The value of the parameter is an [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) expression. The URI template receives the type of the object (user, team) to be generated in the `kind` parameter, and the identifier of the object to be generated in the `name` parameter.  #### factories  In the `factories` parameter, you can specify the resource types that can be generated by the external generator set in the `factory` parameter. It takes the value of one or more strings from the following: `user`, `team`.  #### depot  Instead of generating a user and team resource, you can randomly select them from a pre-created inventory. In this case, the URL of the CSV file containing the resources can be specified in the `depot` parameter. The value of the parameter is an [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) expression. The URI template receives the type of the object (user, team) to be generated in the `kind` parameter.  The first line of the CSV file contains the resource property names, the following lines, on the other hand, contain the relevant data. In the case of nested properties, a \".\" character separates the elements of the property name (e.g. address.formatted).  #### depots  In the `depots` parameter, you can specify the purpose of the external source set in the `depot` parameter. It takes the value of one or more strings from the following: `user`, `team`.  #### sheet  You can randomly select the user data from a Google Sheets document. In the `sheet` parameter, you can specify the identifier of a public Google Sheets document. The first row of the table contains the user property names, the following rows contain the relating data. In the case of nested properties, a \".\" character is used to separate the elements of the property name (e.g. address.formatted).  The tenant named `gods` is an example for the use of the `sheet` parameter. It provides the user data in a [public Google Sheets](https://docs.google.com/spreadsheets/d/1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY/) document. In this case, the identifier of the sheet is `1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY`, and the associated TXT record is:  ``` gods    120 IN  TXT \"sheet=1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY\" ```  #### script  You can automatically insert a custom JavaScript file in the login.html, consent.html, and test.html pages. The URL of this file can be specified in the `script` parameter. By inserting a custom JavaScript file, you can also integrate a client-side random user generator.  #### summary  You can provide a short, one-line description, a watchword for the tenant in the `summary` parameter. It appears on the tenant's startup page and all the pages that contain a list of available tenants.  #### about  To provide a detailed description of the tenant, use the `about` parameter. If it takes the value of a URL, the description is downloaded from the given URL; otherwise the value is the description itself. The description may have markdown formatting.  #### attribution  It is an external data source. If you use a random user generator, you can specify the attribution in the `attribution` parameter. The attribution may have markdown formatting, that is, you can highlight any element or provide a link to an external source:  ``` randomuser  120 IN  TXT \"attribution=User data generated using [RANDOM USER GENERATOR](https://randomuser.me/).\" ```  #### logo  It is the URL of the tenant's logo. The image at this address appears in the address bar of the tenant's webpages.  #### favicon  Use the `favicon` parameter to provide the URL of the favicon. The image at this address appears as a shortcut icon in the browser when a user visits the tenant's webpages.  ### Examples  PhantAuth offers several examples for creating a custom tenant. They are ready-to-use tenants, although primarily created to show examples for customization.  #### faker  A [PhantAuth Faker](https://phantauth.net/_faker) tenant contains a generator built on the JavaScript Faker library. The generator runs on the serverless deployment platform of [ZEIT Now](https://now.sh), available free of charge. Its source code is accessible in the [phantauth-faker](https://github.com/phantauth/phantauth-faker) GitHub repository. Its DNS configuration is:  ``` faker.phantauth.net. 120    IN  TXT \"factories=team\" faker.phantauth.net. 120    IN  TXT \"factories=user\" faker.phantauth.net. 120    IN  TXT \"flags=small\" faker.phantauth.net. 120    IN  TXT \"factory=https://phantauth-faker.now.sh/api{/kind,name}\" faker.phantauth.net. 120    IN  TXT \"userinfo=Dream Team\" faker.phantauth.net. 120    IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/united/bootstrap.min.css\" faker.phantauth.net. 120    IN  TXT \"logo=https://phantauth-faker.now.sh/faker-logo.svg\" faker.phantauth.net. 120    IN  TXT \"name=PhantAuth Faker\" ```  #### chance  A [PhantAuth Chance](https://phantauth.net/_chance) tenant contains a generator built on the JavaScript Chance library. The generator runs on the serverless deployment platform of [ZEIT Now](https://now.sh), available free of charge. Its source code is accessible in the [phantauth-chance](https://github.com/phantauth/phantauth-chance) GitHub repository. Its DNS configuration is:  ``` chance.phantauth.net. 120   IN  TXT \"flags=small\" chance.phantauth.net. 120   IN  TXT \"name=PhantAuth Chance\" chance.phantauth.net. 120   IN  TXT \"factory=https://phantauth-chance.now.sh/api{/kind,name}\" chance.phantauth.net. 120   IN  TXT \"factories=team\" chance.phantauth.net. 120   IN  TXT \"factories=user\" chance.phantauth.net. 120   IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/united/bootstrap.min.css\" chance.phantauth.net. 120   IN  TXT \"logo=https://phantauth-chance.now.sh/chance-logo.png\" ```  #### casual  A [PhantAuth Casual](https://phantauth.net/_casual) tenant contains a generator built on the JavaScript Casual library. The generator runs on the serverless deployment platform of [Auth0 Webtask](https://webtask.io), available free of charge. Its source code is accessible in the [phantauth-casual](https://github.com/phantauth/phantauth-casual) GitHub repository. Its DNS configuration is:  ``` casual.phantauth.net. 120   IN  TXT \"logo=https://www.phantauth.net/logo/phantauth-logo-gray.svg\" casual.phantauth.net. 120   IN  TXT \"name=PhantAuth Casual\" casual.phantauth.net. 120   IN  TXT \"factory=https://wt-51217f7b3eee6aead0123eeafe3b83e8-0.sandbox.auth0-extend.com/user{?name}\" casual.phantauth.net. 120   IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" ```  #### gods  For the [Greek Gods](https://phantauth.net/_gods) tenant, the user data is contained in a [public Google Sheets](https://docs.google.com/spreadsheets/d/1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY/) document. Its DNS configuration is:  ``` gods.phantauth.net. 120 IN  TXT \"attribution=God pictures come from  [Theoi Project](https://www.theoi.com/), a site exploring Greek mythology and the gods in classical literature and art.\" gods.phantauth.net. 120 IN  TXT \"name=Greek Gods\" gods.phantauth.net. 120 IN  TXT \"flags=medium\" gods.phantauth.net. 120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/sandstone/bootstrap.min.css\" gods.phantauth.net. 120 IN  TXT \"logo=https://cdn.staticaly.com/favicons/www.theoi.com\" gods.phantauth.net. 120 IN  TXT \"sheet=1Xa4mRcLWroJr2vUDhrJXGBcobYmpS8fNZxFpXw-M9DY\" ```  #### randomuser  The [RANDOM USER](https://phantauth.net/_randomuser) tenant uses the popular https://randomuser.me service to generate random users. The randomuser.me service is called on the client side, the call is contained in the [randomuser.js](https://www.phantauth.net/selfie/randomuser.js) script given in the `script` parameter. Its DNS configuration is:  ``` randomuser.phantauth.net.   120 IN  TXT \"attribution=User data generated using [RANDOM USER GENERATOR](https://randomuser.me/).\" randomuser.phantauth.net.   120 IN  TXT \"script=https://www.phantauth.net/selfie/randomuser.js\" randomuser.phantauth.net.   120 IN  TXT \"flags=small\" randomuser.phantauth.net.   120 IN  TXT \"name=RANDOM USER\" randomuser.phantauth.net.   120 IN  TXT \"logo=https://cdn.staticaly.com/favicons/randomuser.me\" randomuser.phantauth.net.   120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/sandstone/bootstrap.min.css\" ```  #### uinames  The [uinames](https://phantauth.net/_uinames) tenant uses the https://uinames.com service to generate random users. The uinames.com service is called on the client side, the call is contained in the [uinames.js](https://www.phantauth.net/selfie/uinames.js) script given in the `script` parameter. Its DNS configuration is:  ``` uinames.phantauth.net.  120 IN  TXT \"attribution=User data generated using [uinames.com API](https://uinames.com).\" uinames.phantauth.net.  120 IN  TXT \"logo=https://uinames.com/assets/img/ios-precomposed.png\" uinames.phantauth.net.  120 IN  TXT \"flags=small\" uinames.phantauth.net.  120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/minty/bootstrap.min.css\" uinames.phantauth.net.  120 IN  TXT \"name=uinames\" uinames.phantauth.net.  120 IN  TXT \"script=https://www.phantauth.net/selfie/uinames.js\" ```  #### mockaroo  The [Mockaroo](https://phantauth.net/_mockaroo) tenant uses the https://mockaroo.com service to generate random users. The mockaroo.com service is called on the client side, the call is contained in the [mockaroo.js](https://www.phantauth.net/selfie/mockaroo.js) script given in the `script` parameter. Its DNS configuration is:  ``` mockaroo.phantauth.net. 120 IN  TXT \"attribution=User data generated using [Mockaroo's Mock APIs](https://mockaroo.com/mock_apis).\" mockaroo.phantauth.net. 120 IN  TXT \"script=https://www.phantauth.net/selfie/mockaroo.js\" mockaroo.phantauth.net. 120 IN  TXT \"logo=https://www.phantauth.net/selfie/kongaroo.svg\" mockaroo.phantauth.net. 120 IN  TXT \"flags=small\" mockaroo.phantauth.net. 120 IN  TXT \"theme=https://stackpath.bootstrapcdn.com/bootswatch/4.2.1/minty/bootstrap.min.css\" mockaroo.phantauth.net. 120 IN  TXT \"name=Mockaroo\" ```  ## Pricing  PhantAuth is a free, open-source, non-profit application. If you find this service useful and can afford, please make a small donation as a contribution to the operation costs (domain registration, service hosting, etc.)  [Donate on Ko-fi](https://ko-fi.com/Q5Q0T7C7) | [Donate on Liberapay](https://liberapay.com/szkiba/donate) | [Donate on PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=VXLCJ3EZRAE7G&source=url)  ## Generator  The basic concept of PhantAuth is that it generates data in a random but deterministic way. To achieve this goal, a so-called pseudorandom number generator (PRNG) is used. Each object type has an identifier (login name for user, client_id for client, etc.) By using a given hash algorithm, the value of the pseudorandom generator seed is produced from this identifier. Then, every property of the given object is generated with the pseudorandom generator started from this seed value. Taking advantage of the special feature of the pseudorandom number generator, also called as deterministic random bit generator (DRBG), that is, it generates the same random value series started from the same seed, the identifier clearly defines the object generated from it. That is, by the use of an identifier and generator, you can regenarate the properties of a given object at any time.  Based on the above concept, PhantAuth is absolutely stateless, and no storage medium is necessary. So, a randomly selected login name will \"exist\", and the properties of the \"associated\" user can be generated.  ### Identifier  In brief, an object is defined by its identifier. The name of the identifier of a user or client object is `sub` or `client_id` used in the OpenID Connect specifications. The name of the identifier property of other PhantAuth-specific objects that are not included in the specifications is `sub`.  The identifier may contain any character.  ### Customization  Sometimes you may want to customize the properties generated from the identifier. Although the identifier may contain any character, and its structure is optional, you can customize the generated values if a certain structure is used.  #### Flags  You can use a variety of flags to customize or give the parameters of certain object properties (user, client, etc.). The flags can be grouped by their effect on the generation of the properties. Basically, a flag is a keyword. You can set more than one flags to affect the generation of a variety of properties at the same time. To separate the flags from one another and the rest of the identifier, you need to use a semicolon `;`:  ``` joe;female;kitten ```  In the above example, the user generated by the user generator is female, and her avatar is a randomly selected sketched kitten avatar. The other features are deterministically generated from the name \"joe\", that is, their values are not affected by the two flags. The [profile page](https://phantauth.net/%7Ejoe%3bfemale%3bkitten) of this example can be found [here](https://phantauth.net/%7Ejoe%3bfemale%3bkitten).  Please note that the flags form part of the identifier, as a different flag allows you to generate a different object.  ##### User gender flags  The following flags modify the gender of the generated user.  Flag | Description --- | --- male | The `gender` property of the generated user is male, independent of the user's name female | The `gender` property of the generated user is female, independent of the user's name guess | The `gender` property is defined on the basis of the generated user's given name (default) nogender | The generated user doesn't have a `gender` property  ##### User avatar flags  The following flags modify the generated avatar image.  Avatar | Flag | Description --- | --- | --- ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQCAwMDAgQDAwMEBAQEBQkGBQUFBQsICAYJDQsNDQ0LDAwOEBQRDg8TDwwMEhgSExUWFxcXDhEZGxkWGhQWFxb/2wBDAQQEBAUFBQoGBgoWDwwPFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhb/wgARCAAgACADAREAAhEBAxEB/8QAGAAAAwEBAAAAAAAAAAAAAAAABQcIBgT/xAAZAQACAwEAAAAAAAAAAAAAAAACBQEDBAb/2gAMAwEAAhADEAAAAC6Xe29GzHjM+gFAVhqJajyCeLlrIXbWPewzZijGPPvG/NwoetBt08tMkn//xAAqEAABBAEDAwMDBQAAAAAAAAABAgMEBREABhIHITETIkEIFWEjMlFxof/aAAgBAQABPwDoBVvmxe3DuSZCnJjKxAaaaBSlwYJcJz8ZSB+VDVjQ3Ni+L+ukOh9LRaS1IkFCSknvhKchJyB/IOB21vOduKNt+TC3LspNpVvHhKWC26koPYqcb4+5I+SSSPOrjpbVN2D1bt+ImJEkMpDjshCXHsqySGjjKRxKR7jnIOuhUaMxtlguVqY7rbi2kxArJCXMcV4wAByB8Z8E6n9TaSv3Wjbv2+zmPuKS0XWWx6SV+AknlkHP41Y9SqSbuqZtX7baR5rZWxzdY/RWvuCnkVd/6A8d9b86uWjd1Pq9gbUfdlR3lx3LFTBOVpUQotj9oTnwfONdEdwsU0lFHcwr+NYT3S5BVYyUSBz9MFaUnlyCQhkrHYgYWdXG762DdoW/ErgtlHMvynkMKkZ8IZUrty+T+AE5Gci26m1CGLO+broZQ0y9JcLcptx2MpIK1IdKSQOXwO5GoHVSss7kzbWqkyovqKWquE/0m3CpWTlSEBXgkY/0+Da9L7fY/wBUNYuXbxp1TupiwjUCe6HIkhtv1g0sEcQVMtuoCwdX93XVT8ytvYMkpT7WltoQpaUgkcClYOCDkeDqvsdoXcKTAuSKiisIsiqYfslAqlzZDZaQhtKQSSjklftHtJSdVzEqC7IiTWiw/FcWy6kkHgtJwpJI7ZBBGc41/8QAJREAAgIABQIHAAAAAAAAAAAAAQIAEQMEEjFBIVEFEyIycYHB/9oACAECAQE/AMsFY6wKqM/WxDiudhNbXqPEyTgYTKxsi4XrrvFY77QgM2omhMNhiMShBrtMJgxvtPc6qOYnhgVvU9/VfsbKocu2FhKF+O8S1NHoZkcvqfzX42nM/8QAIhEAAgICAgICAwAAAAAAAAAAAQIAEQMhBDESIhNBBTJx/9oACAEDAQE/ALLHcXB600PEXxu4cSeOonFyL4mtE9/yLjJNHUyLQI7FQkra9kTj8la+I/e9wJ61ZsxwqYmLH9RG5pK0q0Zg5ATMrt0DFfVg2J+W5nr8SffcB1P/2Q==) | ai | [AI](https://thispersondoesnotexist.com/) type generated, photo-like avatars (default) ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABelBMVEX////uuIw6TFomLDQ4SljuuYovQ1Hvuo5KMSztuI4xRFIxQ1DsuY3storvuY3+///zvY8nLTLc4ePx17zvxqPzvpP2wZHvuYrVpnyjfVycdlw1SFcyRlWWc1QjN0YqOEMoLDVMMCxILipFKyb6/Pv9/vn3+Pju8vPu8PDo6+337d/Bxcets7eHkZn1wZXotYrutonsuYiViobQonj7///79+/28unx4M3y2cbx3MO3v8Ozq6nov5ruvpLktYvxuIfpt4bbqYCnlIDQo33MoHlxdXmEd3O+k3C5kGqlgGA7TVueeVltXFktP0p2VURrTD0qNDsmMTgoLjIfJS8iKC1DMyX9/vvl6evq6Of28OHb1djb1NjEycvGwr/Jwb+yub3Cu7nu0rjt0bi3sazfvp7evZzpvJPdtZN+ipPpvJKdko/uvIx1gYrisIVxfIXRonqJe3pWZXGCb2iuhWRDU1+dd11pV1SGZE6BYU4tQE5iT0pXQkFDLylBKSPfP9FbAAABsklEQVQ4y62SV1fCMBhAm5C0tLWlIFOGAoqAAgLuvfdW3Hvvvcd/NynnCJLy5n3p+XJv25y03D+zttOV+Zy+qC2jNz6+w6FgMGjeNPbb4aA5T3jPyNeGQm9VhOfHWXM4wnpL19erA1AqhNnQoYUt7uacIB9UOOcyHMv0GFE0EEU8NmoQvFyqjqQAgOBwqNdGwYNz3ONxY+z2eMadmWbGt/T2ZDUNEwQt23PawgSVLqBOTNFXTE2oAFcaBWBoGBCGh4BR0JGmsimVaqLXdAcT1O0rRCjZW4UGB+z3Wmmlt2rJpEaOKt1qYZ/AdfcB4M/l/AD0dZORJd4vioLfL4hif5wzpE0RscuFRaWNK0P8RAVAPV/nytF87B4YcB9ZynmbzU5P0m6zGdloAgXq7fR3sNcHUCJa6hu8kATtCsZKezSAIGr46zt9EPL8SGww1TsYG+F5CKXOYr9KPJSkhWXT0pJpeUGSyOiLFW32hiwgXppfrCEszks8IgtXBR+R9YCvtpoI1mr+PXGGoBwp3iFBKgS++ycIvVu/QSOigVeeMenMyPqMdkuCSVnWvVWWJ/WgkbofGhc3SydvBmYAAAAASUVORK5CYII=) | sketch | sketched photo-like [avataaars](https://getavataaars.com/) avatars ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQDAwMDAgQDAwMEBAQFBgoGBgUFBgwICQcKDgwPDg4MDQ0PERYTDxAVEQ0NExoTFRcYGRkZDxIbHRsYHRYYGRj/2wBDAQQEBAYFBgsGBgsYEA0QGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBj/wgARCAAgACADAREAAhEBAxEB/8QAGAAAAwEBAAAAAAAAAAAAAAAABAcIBgP/xAAZAQEAAwEBAAAAAAAAAAAAAAAFAwQGAAH/2gAMAwEAAhADEAAAAKqCXmKa6P3Ur6dnoLS3qPAoU9InlVzAmWDq+q42gRzMJepNsBxZvCPWhP8A/8QALRAAAQQBAwMCAwkAAAAAAAAAAQIDBBEFAAYSByExE0EUFVEWIiMyQmFxkbH/2gAIAQEAAT8A+bIwOSlTA20iGpbzrzjaAXClKeXbt3rW8989V944c5+LGcfxU0r9CKy4GwGQriApI48/BNm71sHq71E2dPZjZfGvyMGshDsSSeaRyIFIJFJJ1Kw70zIJf2rFfeZUn8RvtTS+xKeRP0I89voT7TszHm4lczmlh1cFL7bJPZRWSKH8CzoTcpBlYrbLO3XlwxFQgzw4kJQoJF/cq6v31Ekqy3zLETNvS47ENbZTIk0W1lDyDYoX7WD5/bT+2mZ60oRkIhkFRWFsZN5pZUfJtKQfP11kus2zoKMWJ+OkyBFYZbRKQsUhSKBUgBXe/NEdxpzqTPlNujb8JhbuNQiPKTOfS1wVVd0+SCBYI1M6m42BDbi7i4QMpIPNccH1BxokKtN0OVV58HWG3jh1vw3JOIeeiLbDhkR5iSSon8vZsitSp7z7LranFEA3V/2f919stvbnxrOcTuc7czDjKGsi36XqJf4CgSixzr9JBujRB1ms+5kt2TJ6JcmQ2FhDbsmgtaU0ORA7C6Jr2urNXrozuCa9siZF+NcQwyQQk0QVEAEkHz4Tr//EACURAAICAQMCBwEAAAAAAAAAAAECAAMRBBIhMlEFExUiMUFxsf/aAAgBAgEBPwCtsEmeaith4GR+kxQzdIyJYhryByBLCQeJpF2glp6U46WENG4nJ+ZYWW7b9TSA2kl4umA9xPH7NvaHR2iwo67lzwe2ZVUKkCAYxPFw6otinAGf5xP/xAAgEQACAQUAAgMAAAAAAAAAAAABAgADBBESIQUxFSJx/9oACAEDAQE/AGTYCUbIlcr7lezKjMLhOMcGWxFZlU82MtlGvTL8FgFp+zifJUx7WCi66lTggyxVKqAM2DPIbp9KOCex3dTow7+Q1jgiU7ykUFVX1bHRHuGZ2cnMtwrkhhk8n//Z) | photo | photo avatars ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAASFBMVEX///AoHCf/4LXP1Yz////EzHL/3K3Tmob/5sRURUXWuppMNzoKBgnWz8Df0rhXhIg+NC0uIyrf5+jz9eTf2cr44sHZ15VMPj4HhT4EAAAAlElEQVQ4y72S2w6CMBBEpYhstRXx+v9/Ko4LS1sgmRfOQzPZOWnSy2FHqgxW8FVJ0vfT+Aw+Q/LL+zvgsy2sVW6BFFyvtRGCCRgcf7gskkJnQncvBZGriBvjSxJhlfSYNreLIoScTaFtOQF4rcDSl3lGzC4AMUb2T4ITQGSFdw2ax/COTf1n3ms9ogorQNGlFBI44QtzCgcBd0pFOQAAAABJRU5ErkJggg==) | dice | pixel art-style [DiceBear](https://github.com/DiceBear/avatars) avatars ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQCAwMDAgQDAwMEBAQEBQkGBQUFBQsICAYJDQsNDQ0LDAwOEBQRDg8TDwwMEhgSExUWFxcXDhEZGxkWGhQWFxb/2wBDAQQEBAUFBQoGBgoWDwwPFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhb/wgARCAAgACADAREAAhEBAxEB/8QAGQAAAgMBAAAAAAAAAAAAAAAABAYDBQgH/8QAGwEAAgMAAwAAAAAAAAAAAAAABQYBAwQAAgf/2gAMAwEAAhADEAAAANaJeOCqOd+iDnkJur0WoZYGhWcmLanlnJDCsyquYXZ9NWmmUpTHqfadDPhj/8QAKhAAAgICAQMDAwQDAAAAAAAAAQIDBAUREgAGIQciMRMVQSNCUXEyUmH/2gAIAQEAAT8Az3cdmbvpoqlmdqsE8dOKGFggaYuY3ck6J0zlNbA2m/J11lO985i+9rmOatHchV2P0nKxmFdnhpvnRXRPtY+V8aPXcnrtnKdmCnat0KkwTlYjhgkeSJ0mMb71vanTsnjzwAIcHz6HeoWb7zyUMZ4S0oIXWWyYDE9kr+8qQvBgSgKga9zHWtazNRZ8pnpnhlcUpLVmIQ+11lW0oVw2wVADOSR5A2RsgDpObF5XkeWSV2klkk1ykdjssQAACT+AAB8AADXSxVIu5ESDEsbeQhkaS5DVGiIyihJZB52eY4qd7CN/r1grAjz1evjK9iI1L1YN9CLgk6mdecaP/idPHp1HkFdEeR01atW9V7ONvQI9TMVXVY2GwxcBzv8AsxTf9G16z3Y9jHRvPQngejChZhM4jaFAP51xIA/JK6A+D1QTKXpoExKvWtyv+k0yKVQ+dc15r4PwAGB2QD/B9P8AsrK0cn937lyy3bKbaKCCNUhjZiWL6ABJ2ToHlrQPJm2x9R8NYvUosljQfuOOb6kPEbLgENrX5IKhgD86K/uJ67m7myncMfAwT16qIA1KA8nsOB7ixHll3sKh0NeXGzpOxe4Z4IMPnM/WnipySWK9yNNgpKkwVCfOw6hGP9+NAkdROskYdGBVgCpHwQev/8QALhEAAQMCBAMGBwEAAAAAAAAAAQIDEQQhAAUxgRJBURMUYXGRoQYQIiMzscHR/9oACAECAQE/AH83WM1TSoEpsDHXn6C2KrPHqOodS4ApIVAGhiAdb9eY3wxldPVNU9U09DawCQdTIsARoZsbcjjM+NjOVUrY+3w8XOb6e8jxicNMTXVrhMFMwehJ12/WKh9x91TrhlRwFvushHaEpSRCZOpm6RtfzGMuVVU1c32hMrIBBmYkfvQHzw22lnOXUKH0uoncWP8ATiu+FlcRXTrEdFct/wDcUFK49VBtogqGhmPQx/MUOUlp7vFQeJYsNbbmPYAXNtIzOkcdQl1j8jZkePUb4zTO6irUKanBSDY9Z5jyGMqR3SrVKZTYT0tNt42+X//EACwRAAIBAwEFBgcAAAAAAAAAAAECAwAEIRESMUFR8AWBkbHB0RATFBUyQqH/2gAIAQMBAT8Ae5P1IiFS3RhJ1znTTuHGvus+pATrrNWF286ja3jf78s0iazTNxFSOzsWbfQUspIPLHHNWu3FKuv7eNKoW6bkw8qm7OJJKN4+9QRFpNlT/dPT0qK22W2239dbhU8ZcBl/Jcj276ubt5D8tMc6t0EUxxjHl8P/2Q==) | kitten | [ROBOHASH](https://robohash.org/)-generated sketched kitten avatars ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAcFBQYFBAcGBQYIBwcIChELCgkJChUPEAwRGBUaGRgVGBcbHichGx0lHRcYIi4iJSgpKywrGiAvMy8qMicqKyr/2wBDAQcICAoJChQLCxQqHBgcKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKir/wgARCAAgACADAREAAhEBAxEB/8QAGQAAAgMBAAAAAAAAAAAAAAAAAAUDBAYB/8QAGgEBAAMAAwAAAAAAAAAAAAAAAAIDBAEFBv/aAAwDAQACEAMQAAAAc9Z7oAAFM8lXmOgr25uzDMTxt5Ku5DQgtxWBpXr/AP/EACgQAAICAQMDBAEFAAAAAAAAAAECAwQRBRIhAAYxEBMiUQdBRXFzwv/aAAgBAQABPwD0BBzgg444Prc1F1p+7PQtiNZzkIoYlEG7ewPhcjwfOP1z1oGqi7BLLQRrETXNkkjZVtpiQiTHOcnB8+Gz6d394J2tQSdKZuu03tOqvsEZ2hvk2DgkHjqHvLQZHENm/WqzGNHMU0yHAZQw+QJU8H7/AJA6m7p0CooD6rTHgKkcgY/QAA603uGC/repaU0FivZoOqSrPGF5OfjkE/Lg8HB6s6VTutKbMCSrNGI5UcZSRQcjcp4JHOD5H31N+Ne1p/2wJ/VLIP8AR6bsPQZ5o5b0E99oo1ijNy1JJsReFQZbhQOAPA6qaJp9F4zSqpXSLJjiiG2NWIwX2jy2ONxyccdf/8QAHxEAAgIBBAMAAAAAAAAAAAAAAQIAAxEQITFBEhMg/9oACAECAQE/APlRgxxvvpWnmYamXqCtj1GrKDJgYjie54bnMLluZ//EACgRAAEEAQICCwAAAAAAAAAAAAECAwQRACExBUEQEhUgIlFhgZGhwf/aAAgBAwEBPwDuvLK26o1f0OeR12klOuv5v0SpYjpsCzdY1OYcTqqj66YqUwgWVjI8tD6ilPLFsocvrDfOzY/kfnE8NjjcE++Nx22z4BWf/9k=) | adorable | [Adorable Avatars](http://avatars.adorable.io/) ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQCAwMDAgQDAwMEBAQEBQkGBQUFBQsICAYJDQsNDQ0LDAwOEBQRDg8TDwwMEhgSExUWFxcXDhEZGxkWGhQWFxb/2wBDAQQEBAUFBQoGBgoWDwwPFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhb/wgARCAAgACADAREAAhEBAxEB/8QAGgAAAgIDAAAAAAAAAAAAAAAAAAcBBAIGCP/EABQBAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAOii6BSAb5InzIaoCqNqGQAtz//EACcQAAIBAwMCBgMAAAAAAAAAAAECAwQFEQAGQRKRBxAhMTJxE1HB/9oACAEBAAE/ANWe03G6OVoKV5un5N6BR9k4GrvaLlayBX0jxBvichlP0Rkeey4IYNrUKQABXgV2I5Zhlj3Ot4wQVG165JwCqwM4J4ZRkHuPKFHllWONCzuQqhRkkn2A1sS2XG12YQV06vn1SIDP4s+46udb4ttwudmanoKgJy8RGDLj1A6uP7+9So8UrxyIVdCVYMMEEe4OvCOgSpvc1ZIARSRjoB4ZsgHsG8/FqgSmvcVZGABVxnrA5ZcAnsV1/8QAFBEBAAAAAAAAAAAAAAAAAAAAQP/aAAgBAgEBPwAH/8QAFBEBAAAAAAAAAAAAAAAAAAAAQP/aAAgBAwEBPwAH/9k=) | mp | simple, cartoon-style silhouetted outline of a person (does not vary by user) ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVPMTn///+hkZWsnqKWhInz8fG3q67o5OVjymXqAAAAoElEQVQoz82OwQ3CMBAEV8ENXCzxdjowHeBHCnBQ/jRB/2TWwjVwq5H2tXOK3HPkLYAoaq9RlwCirNeFNnCqyoUWcM7jcxQpwX7upzdWqcHciJIC5kasLcAb+DVudPwaNzp+pOBO5S1wx6/HXeCOX7e3wN3+caPbP879b/4oetoPSt447Ac1b/SCFFJ4o6/4ocXYsB9+G/bD3MAPcwM/kC/KhCQv+Oa0WgAAAABJRU5ErkJggg==) | identicon | a geometric pattern based on an email hash ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAB2lBMVEXw3/Q3t350dHTn1+uwo7LAssOnp6dVVVWhoaGamprs3PDp2e3j0+ZxcXHZyt2UlJQ1sXlwcHBcW1zTxNapnauMjIyHfol3b3lvb29qampoZ2jh0eTez+K5ubmmm6iakJyYj5qTiZV+mJOSkpKIh4h8fHx4eHg0p3RsbGxiYGJQUFAgbUvQwdPOwNLNzc3Hucq/vcC5rbu4q7u2qrmVjJeWlpaTk5ORh5OPiZGPj4+LhoxylouJgYuAd4JzioB+dYB+fH96eHs0rXcwoW9uZ29Chmg7hWVkY2VgW2I4c1lOTU9MTEzJu8y9r8C0p7e1tbWyqbWiqa+rn66ro62qqqqkmKahl6Ock56MnJyFgYWEhIR1hn98c35lf3ZzbnRJhmsvmGlUdmg4jGctkmVkXWVRaV9fX180eltEa1kmf1dFZVdVUVZHR0f////o2OzVytvY2NjT0tPKvs3AvMjCtMXCu8Sqsbeor7WxsbGtobCurq6mqqicn6ajo6Oenp6OjZWJiYlymohwj4dxioVDt4Nil4N4i4OAgIAzqXQ6onRcfm85mW5LgWw6kWtkbGhgaGdAgWRUbGMwimJNZF5KZFxZWVlLVFBJRUo9UEg5UEgfZ0c8PDw7OTsgQzTXmnPvAAACSUlEQVQ4y42ShXPiQBSH325ISBqCe4sWKFJ3B4pD3d2u3p67u7v7/3pLgB5Q5ua+yWQy+X37due9hf9CXl/1z/zC+XPjZyBHK4BGVi6Mn+64EV0Wi1BWoCahnJrmxmaZLKinAKrpKykeQDIDwE9ZLoNItWGgiQe+YWCZgpaJOvT47OSwPGhINjY3ips1qf0Zv3qErx81bMHVCEJoUxvVO7p+9VxrgSyrWIqPjF59FdADH+tIXhcIPOxP4CO11waEUR8RjH6887VL/mo/gFDkxxBCKfxZKsXeWSJsYSwVH+Hta4TW9yMBRFDuZXAGY5MWIGne8Ru9RNgm5QlkuWgcYJMaq3xWANA4ZrRp6fYzVMK6GadxkpZDHvoUKmNX9TOhKRpH34Nve8fShy+/+zbUvn4oYc6UKghx2/Vsh6lSoSp6QLLYS/Lqg4rUfFduLlluPkJovuKlGLF+ejc9uHSfVLgrOxE3HAq17O7gEyXK8ibca6OLT0C1uxnF01Dn2BoS2WAZhgvrG46b4GLYWmFsZS2uzAkxXQfHkn+5ccoWdIxCZ5oeJGmBF5yC5Wo7JWL5MMfc4ViVJY7+MvS+e5HrIVeAUN/TybDu7pAlhop4fpE3L87lDqgyGiSUJuRxrzid8xKRW07nBCzcloBIt8IB0Mq4OC0UI8O6vDB7D1MAU71WvkSQuIz5TjTpFG1wkvYOoTCkVXclwaXozec2qVmtLY81/WnhsEb8NJhUgkdwlObVCZXZ4/ENA+ESTbfa7V1lAk23tdvtQQr+AEpRWa/mX8zUAAAAAElFTkSuQmCC) | monsterid | a generated \"monster\" with different colors, faces, etc. ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQDAwMDAgQDAwMEBAQFBgoGBgUFBgwICQcKDgwPDg4MDQ0PERYTDxAVEQ0NExoTFRcYGRkZDxIbHRsYHRYYGRj/2wBDAQQEBAYFBgsGBgsYEA0QGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBj/wgARCAAgACADAREAAhEBAxEB/8QAGwAAAQQDAAAAAAAAAAAAAAAABAMFBgcBAgj/xAAbAQACAwEBAQAAAAAAAAAAAAACAwAEBgcBBf/aAAwDAQACEAMQAAAA7bDwNf1URYFK7aFah061OMmdYZHaxjHR6yMLmEsbVQ8o1RuMQhGZD//EAC4QAAEDAwMBBwIHAAAAAAAAAAECAwQFESEABhIHEyIxUVKR0kGiFSMkNGFiof/aAAgBAQABPwD8Vlvy0R4pbF0laluXISBbFhbxv5/TTm4JLTpQZcXH9VfLTm55KGlLEqKbD0K+WqDvw1Sqv054Nh1CO0Spu4BSDYggk+ac3zc4Fs06euQ6+Uryhk/6U63HRRL620eGjY8KpUidBck1iryePNiV3vygmwNgUoAJKuQXcHGOn9I/QVmpVzaEbblbiVYx6ezG4FMmJ61FKbpAGQoqss4462nNVG3u6ortyiuj729bOqTbzs/tFjDIt76mVVbFUkJehurY5XQ+xZfdsLhSb8r8uXgCLWzpdWXI4oiwng0T33n7NpCfrZJPMny7oH86jTRG3chSVYVHeH3tapPV52lKfLRbd7ZHCy74ze+DpXWCSpfK8T2V8tHq7IN/2nsr5af6lokPNPHsm1tIUm7dxfkQT4k+lOv/xAAiEQACAgECBwEAAAAAAAAAAAABAgARAwQSEyExQWGBwfD/2gAIAQIBAT8A3Q5wIdQBMOoGW67QtamZCoQFW5xypw3u5/u00Brf6+wMNpuEi+sYius0Zrf6+zjCiDKTzKTzEdUFLP/EADARAAECBAIGCQUAAAAAAAAAAAIBEQADBSEEBgciMUFhkRITVGKSwcLS4UJRcoGh/9oACAEDAQE/AJA9Y99kDSTJHRV5fMDRTJWf+fMValzKb0FNXQnbdsZ7ftIoKocwkXh5xgJc6ZiSGfL1b/TZtyou/nGFHEDUEFJbBd9WyJ+W/nGkRhDCt3vTGVnmTDbh5xLA0HZaJYH0ktGkzVDCP3/TGX81FSJxTEBDQkuiq2zjeE0vn2UfEvthNMB9lHxL7YzPnebXylqYIAi7IivtZ72+0f/Z) | wavatar | generated faces with varying features and backgrounds ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAABlBMVEVLAmn9LdWXmTS+AAAAMUlEQVQI12N4wMDAj0wUyCATDAUyDMgE/wMEARbDIOQbmD8gEx/kkQmZApkCJIIwAAAZjxw4Pi/EJgAAAABJRU5ErkJggg==) | retro | awesome generated, 8-bit arcade-style pixelated faces ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wgARCAAgACADAREAAhEBAxEB/8QAGgAAAQUBAAAAAAAAAAAAAAAACQABBgcIBP/EABkBAAIDAQAAAAAAAAAAAAAAAAAFAwQGAf/aAAwDAQACEAMQAAAAKmFTQT2dNB19GAcj3fTwWbgRZRgG/Z38htKyALMogqCxfyBdakdVZv8A/8QAKBAAAQMDBAEEAgMAAAAAAAAAAgEDBAUGEQAHCBIhEBMiMRQkMkJS/9oACAEBAAE/ANbv71SdsatRILFtzqutSkjH98U6MopKiIiH5yXlVxj+uqe6+9BYclMDGkmCE4yLnuIBY8j2wmcfWcevNTlQtyXJKsq3ak/T4dEnKD8qKRNGclvIkvuf5RVIRQcYUVJV1wb5PXJet1zbBvGpFWjKN+ZSqm8Qm9gfJsmafz+OSQl+SYJF9d+OJNfi7n3XV27br9xU2rVBZ8OTQBjGgA453eB4XF7IY5JBwnVdcCuOVXS8I+69RzTKE2zJYosJ0wKU+hEbSuPIHxFBHI4+1L15N7k1javbF2r0IYS1A5Tcb94FMUAhMjUQQh7lgPrKa4b7/wC4q3jaVty3YMbbFme9RTMWA7rLfZekMNqXZXEVTEkFcIOkXOv/xAAlEQABAwEIAgMAAAAAAAAAAAABAgMEEQAFEBITITFBMlFCccH/2gAIAQIBAT8Ast0INKWHG+MJiMkZ5XfA/bXjDbaGqz4+sZN43olDTd2aSQkHNqBRJPxpl6913s/eDsiO227TOAMxGwJ7oPVeK4xmkvOpbUaV2tNitQyW6kq6+sP/xAAkEQABAwQBAwUAAAAAAAAAAAABAgMRAAQFIRASMXETFEFRof/aAAgBAwEBPwCm2usEzXjnCYfqb9w62VSNa1FZjGt249dgQmYI5x+Xtk26G3DBSIOu+jG/MTWWyiLlsMt7+z2/ObFlFw+lpwwDWSsbeyBbBJX8eOP/2Q==) | robohash | a generated robot with different colors, faces, etc. ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAAA1BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAAtJREFUCNdjGOQAAACgAAH4BzM6AAAAAElFTkSuQmCC) | blank | a transparent PNG image   | notfound | return an HTTP 404 (File Not Found) response   | noavatar | the user will not have a `picture` property  ##### Client logo flags  The following flags modify the generated logo.  Logo | Flag | Description --- | --- | --- ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAJFBMVEX/VyL76ef+dkz71s774t39noL8uqf9kXD+glz/Zjb8xrf9qZHgm7oqAAAAlElEQVQoz6XNwQ0CMQwEwPUhIZ5rgcQXRAOUcCUcJVACHVACdEAJlMh5E5Dlzz1YR4k0iWN4yQ9WFWALQPgSWAYgALh1wBxa7E/BC5jAIyICAHbmbhNgM7Dd6GTAA5HTXa5KuVSwsQL/Bx8rqCowfbG1Agzw3HENmNAzODwWU4fA04wG7A/eJviKHeCCJsMea29Q8gH9RxXZMd8OgAAAAABJRU5ErkJggg==) | icon | [Game-icons.net](https://game-icons.net/) icon as a logo (default) ![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBAUEBAYFBQUGBgYHCQ4JCQgICRINDQoOFRIWFhUSFBQXGiEcFxgfGRQUHScdHyIjJSUlFhwpLCgkKyEkJST/2wBDAQYGBgkICREJCREkGBQYJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCT/wgARCAAgACADAREAAhEBAxEB/8QAGQAAAwADAAAAAAAAAAAAAAAAAwQGAgUH/8QAGAEBAQEBAQAAAAAAAAAAAAAABgUEAwL/2gAMAwEAAhADEAAAAASHNXa056c8HP8ANkeusPyLOLuuNvc5byaaDbHQy6XH2GuA1ZxYPrmmEZP/xAAuEAABAwIFAwIEBwAAAAAAAAABAgMEBREAITFBUQYScQciFGGBoRMyM4KRksH/2gAIAQEAAT8A9HPT1mndMtPSWEKkPgPvFY3Oif2jFIpIlTZbIUoMpUlBUDmfbfI83++KlCXSHwxEJSJC9ASeVKt87ZeABtj1YoEiu0B2LNYR8THBehu6kLAuW720UBa17XANztSOokwaOSMwoFSlk2CTve+nP1x03W2GWnXJDqWUuO5FZ7ArPM57knTxpiqVVpVUgFVz2lRBPix+x+xx1xKjSobamFBStAUkHOxIz8gHBpyZcj8U+1squv3WCc/GoJH8njOJGbkLKVuraQpAUhIV+Ygg9pO4NsxwPGKhAkxgiK4opfjICw4q/cogDjQk2H1POH5lReaWmSsPFA7UWCQCom225sc+LnI3t05UY/UNFiVRkBRdQEvI07XAlQWP7km3BBxGmOxYJi/DtusKIUF6qQf9Gmp2xUJTD6OyO4p1Q/UWSVdxyyGW1uecdTTo9Ao8uovaMBYabXY9zujQA+V0g22F8f/EACwRAAECBQICCgMAAAAAAAAAAAECBAADESExEkEFYRMUMlFxkcHh8PEigdH/2gAIAQIBAT8A4k5UFdCnAz4+0NXC1MES0mn5H+w0dFpImrVemK3vT6MNn6nZKJhqoYhwhap9KXMM2iGzWWiYoAm+dztztHHmpS11p2Vf9j2hlMMtwlQ2IhHCZ8qdrVhO+ceQMO19aWrWvSUdkd45czmGM2aUKaTb6sD09YZcJWp2lGkgA38AeflCp5nNqitabZsKYia0UhJHbBNlYp31r8pCGhTN6RJ1KF1KJsOX0IW4UJSp69sV54PzIBMf/8QAKxEAAgECBAQFBQEAAAAAAAAAAQIRAAMEBSExE0FRYRIicYHBMlKRodHw/9oACAEDAQE/AMutjA4dfvfU9ulYu4i3uKwBaNPzRspi2Qt3n0msyyyy+HLWOWtXcKtxg5MAVnPFu32aypIUAbToOf73rIvExdWO66ex1rBWHCOj9Kv51hnAVWktsJ117bilThongSZPm7aTPxWIawFGKtkQDqff+0+Y20wzXZBkae9ZeFW8HYjXrMT0nl27GKwuJ494XSeGyyGT6vFGxEH4NHHlbbC6ptqfKiBRJjn6eugoJwXKqYG8Dr0P+MSB1j//2Q==) | fractal | [Electric Sheep](https://electricsheep.org/) fractal as a logo  ##### `Group` size flags  The following flag modify the sizes of the generated team (group of users) and fleet (group of clients).  Flag | Size --- | --- tiny | 5 (default) small | 10 medium | 25 large | 50 huge | 100  #### Name  In most cases, the generated objects have a full name, which is generated from the identifier. Instead of being generated, the full name can be produced from the identifier, if the identifier contains at least one period (`.`) or space (` `) character. In such cases, these characters play the role of separator between the parts of the full name (e.g. family name, given name). That is, the full name isn't randomly generated from the identifier but, by taking the separator characters into account,  it is produced from the single parts of the full name (with capitalised initial letters). For this purpose, it is advised to use a period character, rather than a space character.  ``` joe.black;sketch ```  In the above example: The full name of the user generated by the user generator is *Joe Black* (and his avatar is a skecthed profile avatar). The [profile page](https://phantauth.net/%7Ejoe.black%3bsketch) of this example can be found [here](https://phantauth.net/%7Ejoe.black%3bsketch).  #### Picture  In most cases, the generated objects have an image (avatar for a user, logo for a client), which is generated from the identifier. The *flags* determine which pre-defined inventory the image comes from (see [flags](#flags)). It can be further customized by the use of [Gravatar](https://gravatar.com).  Each object has a generated unique email address (`email` for a user, `logo_email` for any other objects). To customize the image of a given object, you need to assign the gravatar image to this email address. By default, an object has a gravatar image, and the generated image is the default value of the gravatar URL only. In other words, as soon as you create a gravatar image to a given email address, that image will appear as the image associated with the given object.  #### Email  A disposable, operational email address suitable for receiving incoming emails is generated to each object. You can use your own email address (e.g. a previously set test email address) instead of a generated email address, if you prefer. In this case, the identifier contains an email address. Consequently, the image associated with the given object is the gravatar image assigned to the email address contained in the identifier.  ``` ivan.test.szkiba@spam4.me ```  In the above example: The email address of the user generated by the user generator is *ivan.test.szkiba@spam4.me* (and his name is *Ivan Test Szkiba*). The [profile page](https://phantauth.net/%7Eivan.test.szkiba%40spam4.me) of this example can be found [here](https://phantauth.net/%7Eivan.test.szkiba%40spam4.me).  ### Custom Generators  PhantAuth can use external data sources and generators as well. The only restriction is that the external generator has to be deterministic. This means that even if called several times, it has to generate the same object to the same identifier.  A special case of external generators is if an external data source is used. In such cases, the properties of a given object can be provided in a comma separated value (CSV) file or a Google Sheets document.  The external data sources and generators can be defined by the use of so-called [tenants](https://doc.phantauth.net/#/tenant). To learn more, please go to chapter [Tenant](https://doc.phantauth.net/#/tenant).
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_tenant__tenantname__get_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_tenant__tenantname__get_200_response::OAI_tenant__tenantname__get_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_tenant__tenantname__get_200_response::OAI_tenant__tenantname__get_200_response() {
    this->initializeModel();
}

OAI_tenant__tenantname__get_200_response::~OAI_tenant__tenantname__get_200_response() {}

void OAI_tenant__tenantname__get_200_response::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_about_isSet = false;
    m_about_isValid = false;

    m_attribution_isSet = false;
    m_attribution_isValid = false;

    m_depot_isSet = false;
    m_depot_isValid = false;

    m_depots_isSet = false;
    m_depots_isValid = false;

    m_domain_isSet = false;
    m_domain_isValid = false;

    m_factories_isSet = false;
    m_factories_isValid = false;

    m_factory_isSet = false;
    m_factory_isValid = false;

    m_favicon_isSet = false;
    m_favicon_isValid = false;

    m_issuer_isSet = false;
    m_issuer_isValid = false;

    m_logo_isSet = false;
    m_logo_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_script_isSet = false;
    m_script_isValid = false;

    m_sheet_isSet = false;
    m_sheet_isValid = false;

    m_sub_isSet = false;
    m_sub_isValid = false;

    m_subtenant_isSet = false;
    m_subtenant_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_r_template_isSet = false;
    m_r_template_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_userinfo_isSet = false;
    m_userinfo_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;
}

void OAI_tenant__tenantname__get_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_tenant__tenantname__get_200_response::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("@id")]);
    m_id_isSet = !json[QString("@id")].isNull() && m_id_isValid;

    m_about_isValid = ::OpenAPI::fromJsonValue(m_about, json[QString("about")]);
    m_about_isSet = !json[QString("about")].isNull() && m_about_isValid;

    m_attribution_isValid = ::OpenAPI::fromJsonValue(m_attribution, json[QString("attribution")]);
    m_attribution_isSet = !json[QString("attribution")].isNull() && m_attribution_isValid;

    m_depot_isValid = ::OpenAPI::fromJsonValue(m_depot, json[QString("depot")]);
    m_depot_isSet = !json[QString("depot")].isNull() && m_depot_isValid;

    m_depots_isValid = ::OpenAPI::fromJsonValue(m_depots, json[QString("depots")]);
    m_depots_isSet = !json[QString("depots")].isNull() && m_depots_isValid;

    m_domain_isValid = ::OpenAPI::fromJsonValue(m_domain, json[QString("domain")]);
    m_domain_isSet = !json[QString("domain")].isNull() && m_domain_isValid;

    m_factories_isValid = ::OpenAPI::fromJsonValue(m_factories, json[QString("factories")]);
    m_factories_isSet = !json[QString("factories")].isNull() && m_factories_isValid;

    m_factory_isValid = ::OpenAPI::fromJsonValue(m_factory, json[QString("factory")]);
    m_factory_isSet = !json[QString("factory")].isNull() && m_factory_isValid;

    m_favicon_isValid = ::OpenAPI::fromJsonValue(m_favicon, json[QString("favicon")]);
    m_favicon_isSet = !json[QString("favicon")].isNull() && m_favicon_isValid;

    m_issuer_isValid = ::OpenAPI::fromJsonValue(m_issuer, json[QString("issuer")]);
    m_issuer_isSet = !json[QString("issuer")].isNull() && m_issuer_isValid;

    m_logo_isValid = ::OpenAPI::fromJsonValue(m_logo, json[QString("logo")]);
    m_logo_isSet = !json[QString("logo")].isNull() && m_logo_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_script_isValid = ::OpenAPI::fromJsonValue(m_script, json[QString("script")]);
    m_script_isSet = !json[QString("script")].isNull() && m_script_isValid;

    m_sheet_isValid = ::OpenAPI::fromJsonValue(m_sheet, json[QString("sheet")]);
    m_sheet_isSet = !json[QString("sheet")].isNull() && m_sheet_isValid;

    m_sub_isValid = ::OpenAPI::fromJsonValue(m_sub, json[QString("sub")]);
    m_sub_isSet = !json[QString("sub")].isNull() && m_sub_isValid;

    m_subtenant_isValid = ::OpenAPI::fromJsonValue(m_subtenant, json[QString("subtenant")]);
    m_subtenant_isSet = !json[QString("subtenant")].isNull() && m_subtenant_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_r_template_isValid = ::OpenAPI::fromJsonValue(m_r_template, json[QString("template")]);
    m_r_template_isSet = !json[QString("template")].isNull() && m_r_template_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_userinfo_isValid = ::OpenAPI::fromJsonValue(m_userinfo, json[QString("userinfo")]);
    m_userinfo_isSet = !json[QString("userinfo")].isNull() && m_userinfo_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;
}

QString OAI_tenant__tenantname__get_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_tenant__tenantname__get_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("@id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_about_isSet) {
        obj.insert(QString("about"), ::OpenAPI::toJsonValue(m_about));
    }
    if (m_attribution_isSet) {
        obj.insert(QString("attribution"), ::OpenAPI::toJsonValue(m_attribution));
    }
    if (m_depot_isSet) {
        obj.insert(QString("depot"), ::OpenAPI::toJsonValue(m_depot));
    }
    if (m_depots.size() > 0) {
        obj.insert(QString("depots"), ::OpenAPI::toJsonValue(m_depots));
    }
    if (m_domain_isSet) {
        obj.insert(QString("domain"), ::OpenAPI::toJsonValue(m_domain));
    }
    if (m_factories.size() > 0) {
        obj.insert(QString("factories"), ::OpenAPI::toJsonValue(m_factories));
    }
    if (m_factory_isSet) {
        obj.insert(QString("factory"), ::OpenAPI::toJsonValue(m_factory));
    }
    if (m_favicon_isSet) {
        obj.insert(QString("favicon"), ::OpenAPI::toJsonValue(m_favicon));
    }
    if (m_issuer_isSet) {
        obj.insert(QString("issuer"), ::OpenAPI::toJsonValue(m_issuer));
    }
    if (m_logo_isSet) {
        obj.insert(QString("logo"), ::OpenAPI::toJsonValue(m_logo));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_script_isSet) {
        obj.insert(QString("script"), ::OpenAPI::toJsonValue(m_script));
    }
    if (m_sheet_isSet) {
        obj.insert(QString("sheet"), ::OpenAPI::toJsonValue(m_sheet));
    }
    if (m_sub_isSet) {
        obj.insert(QString("sub"), ::OpenAPI::toJsonValue(m_sub));
    }
    if (m_subtenant_isSet) {
        obj.insert(QString("subtenant"), ::OpenAPI::toJsonValue(m_subtenant));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_r_template_isSet) {
        obj.insert(QString("template"), ::OpenAPI::toJsonValue(m_r_template));
    }
    if (m_theme_isSet) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_userinfo_isSet) {
        obj.insert(QString("userinfo"), ::OpenAPI::toJsonValue(m_userinfo));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    return obj;
}

QString OAI_tenant__tenantname__get_200_response::getId() const {
    return m_id;
}
void OAI_tenant__tenantname__get_200_response::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_id_Valid() const{
    return m_id_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getAbout() const {
    return m_about;
}
void OAI_tenant__tenantname__get_200_response::setAbout(const QString &about) {
    m_about = about;
    m_about_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_about_Set() const{
    return m_about_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_about_Valid() const{
    return m_about_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getAttribution() const {
    return m_attribution;
}
void OAI_tenant__tenantname__get_200_response::setAttribution(const QString &attribution) {
    m_attribution = attribution;
    m_attribution_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_attribution_Set() const{
    return m_attribution_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_attribution_Valid() const{
    return m_attribution_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getDepot() const {
    return m_depot;
}
void OAI_tenant__tenantname__get_200_response::setDepot(const QString &depot) {
    m_depot = depot;
    m_depot_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_depot_Set() const{
    return m_depot_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_depot_Valid() const{
    return m_depot_isValid;
}

QList<QJsonValue> OAI_tenant__tenantname__get_200_response::getDepots() const {
    return m_depots;
}
void OAI_tenant__tenantname__get_200_response::setDepots(const QList<QJsonValue> &depots) {
    m_depots = depots;
    m_depots_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_depots_Set() const{
    return m_depots_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_depots_Valid() const{
    return m_depots_isValid;
}

bool OAI_tenant__tenantname__get_200_response::isDomain() const {
    return m_domain;
}
void OAI_tenant__tenantname__get_200_response::setDomain(const bool &domain) {
    m_domain = domain;
    m_domain_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_domain_Set() const{
    return m_domain_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_domain_Valid() const{
    return m_domain_isValid;
}

QList<QJsonValue> OAI_tenant__tenantname__get_200_response::getFactories() const {
    return m_factories;
}
void OAI_tenant__tenantname__get_200_response::setFactories(const QList<QJsonValue> &factories) {
    m_factories = factories;
    m_factories_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_factories_Set() const{
    return m_factories_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_factories_Valid() const{
    return m_factories_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getFactory() const {
    return m_factory;
}
void OAI_tenant__tenantname__get_200_response::setFactory(const QString &factory) {
    m_factory = factory;
    m_factory_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_factory_Set() const{
    return m_factory_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_factory_Valid() const{
    return m_factory_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getFavicon() const {
    return m_favicon;
}
void OAI_tenant__tenantname__get_200_response::setFavicon(const QString &favicon) {
    m_favicon = favicon;
    m_favicon_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_favicon_Set() const{
    return m_favicon_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_favicon_Valid() const{
    return m_favicon_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getIssuer() const {
    return m_issuer;
}
void OAI_tenant__tenantname__get_200_response::setIssuer(const QString &issuer) {
    m_issuer = issuer;
    m_issuer_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_issuer_Set() const{
    return m_issuer_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_issuer_Valid() const{
    return m_issuer_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getLogo() const {
    return m_logo;
}
void OAI_tenant__tenantname__get_200_response::setLogo(const QString &logo) {
    m_logo = logo;
    m_logo_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_logo_Set() const{
    return m_logo_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_logo_Valid() const{
    return m_logo_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getName() const {
    return m_name;
}
void OAI_tenant__tenantname__get_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_name_Valid() const{
    return m_name_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getScript() const {
    return m_script;
}
void OAI_tenant__tenantname__get_200_response::setScript(const QString &script) {
    m_script = script;
    m_script_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_script_Set() const{
    return m_script_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_script_Valid() const{
    return m_script_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getSheet() const {
    return m_sheet;
}
void OAI_tenant__tenantname__get_200_response::setSheet(const QString &sheet) {
    m_sheet = sheet;
    m_sheet_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_sheet_Set() const{
    return m_sheet_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_sheet_Valid() const{
    return m_sheet_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getSub() const {
    return m_sub;
}
void OAI_tenant__tenantname__get_200_response::setSub(const QString &sub) {
    m_sub = sub;
    m_sub_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_sub_Set() const{
    return m_sub_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_sub_Valid() const{
    return m_sub_isValid;
}

bool OAI_tenant__tenantname__get_200_response::isSubtenant() const {
    return m_subtenant;
}
void OAI_tenant__tenantname__get_200_response::setSubtenant(const bool &subtenant) {
    m_subtenant = subtenant;
    m_subtenant_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_subtenant_Set() const{
    return m_subtenant_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_subtenant_Valid() const{
    return m_subtenant_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getSummary() const {
    return m_summary;
}
void OAI_tenant__tenantname__get_200_response::setSummary(const QString &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_summary_Valid() const{
    return m_summary_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getRTemplate() const {
    return m_r_template;
}
void OAI_tenant__tenantname__get_200_response::setRTemplate(const QString &r_template) {
    m_r_template = r_template;
    m_r_template_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_r_template_Set() const{
    return m_r_template_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_r_template_Valid() const{
    return m_r_template_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getTheme() const {
    return m_theme;
}
void OAI_tenant__tenantname__get_200_response::setTheme(const QString &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_theme_Valid() const{
    return m_theme_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getUserinfo() const {
    return m_userinfo;
}
void OAI_tenant__tenantname__get_200_response::setUserinfo(const QString &userinfo) {
    m_userinfo = userinfo;
    m_userinfo_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_userinfo_Set() const{
    return m_userinfo_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_userinfo_Valid() const{
    return m_userinfo_isValid;
}

QString OAI_tenant__tenantname__get_200_response::getWebsite() const {
    return m_website;
}
void OAI_tenant__tenantname__get_200_response::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAI_tenant__tenantname__get_200_response::is_website_Set() const{
    return m_website_isSet;
}

bool OAI_tenant__tenantname__get_200_response::is_website_Valid() const{
    return m_website_isValid;
}

bool OAI_tenant__tenantname__get_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_about_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_attribution_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_depot_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_depots.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_domain_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_factories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_factory_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_favicon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issuer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_script_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sheet_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subtenant_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_userinfo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_tenant__tenantname__get_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_issuer_isValid && m_sub_isValid && true;
}

} // namespace OpenAPI
