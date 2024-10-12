from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_autocomplete_post_request import AddressAutocompletePostRequest
from openapi_server.models.contact_enrich_post_request import ContactEnrichPostRequest
from openapi_server.models.email_enrich_post_request import EmailEnrichPostRequest
from openapi_server.models.phone_enrich_post_request import PhoneEnrichPostRequest
from openapi_server import util


async def address_autocomplete_post(request: web.Request, galaxy_ap_name=None, galaxy_ap_password=None, galaxy_search_type=None, body=None) -> web.Response:
    """Search

    ###### *Click on the grey search box above, to view sample request/response objects for Address Autocomplete Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIAddressAutoComplete  2.  Add search criteria to your request.     ~~~html             {                 \&quot;Input\&quot;:\&quot;1821 Q\&quot;             }     ~~~  3.  Submit your search  The JSON request should have parts of the address.  + &lt;code&gt;Input&lt;/code&gt; &#x3D; null (optional, string) ... address.

    :param galaxy_ap_name: e.g. Key
    :type galaxy_ap_name: str
    :param galaxy_ap_password: e.g. Secret
    :type galaxy_ap_password: str
    :param galaxy_search_type: e.g. DevAPIAddressAutoComplete
    :type galaxy_search_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddressAutocompletePostRequest.from_dict(body)
    return web.Response(status=200)


async def contact_enrich_post(request: web.Request, galaxy_ap_name=None, galaxy_ap_password=None, galaxy_search_type=None, body=None) -> web.Response:
    """Search

    ###### *Click on the grey search box above, to view sample request/response objects for Contact Enrichment Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIContactEnrich  2.  Add search criteria to your request. At least two are required: Name, Phone, Address, or Email.     ~~~html             {                 \&quot;FirstName\&quot;: \&quot;John\&quot;,                 \&quot;MiddleName\&quot;: \&quot;T\&quot;,                 \&quot;LastName\&quot;: \&quot;Lawrence\&quot;,                 \&quot;Dob\&quot;:\&quot;\&quot;,                 \&quot;Age\&quot;: 0,                 \&quot;Address\&quot;: {                     \&quot;addressLine1\&quot;:\&quot;123 Q Street\&quot;,                     \&quot;addressLine2\&quot;:\&quot;Sacramento, CA\&quot;                 },                 \&quot;PhoneNumber\&quot;:\&quot;\&quot;,                 \&quot;Email\&quot;:\&quot;\&quot;             }     ~~~  3.  Submit your search  A complete list of JSON request properties follows.  + &lt;code&gt;FirstName&lt;/code&gt;&#x3D; null (optional, string) ... First name.  + &lt;code&gt;MiddleName&lt;/code&gt; &#x3D; null (optional, string) ... Middle name or middle initial.  + &lt;code&gt;LastName&lt;/code&gt; &#x3D; null (optional, string) ... Last name.  + &lt;code&gt;Dob&lt;/code&gt; &#x3D; null (optional, string) ... Date of birth (format: MM/DD/YYYY).  + &lt;code&gt;Age&lt;/code&gt; &#x3D; null (optional, int) ... Age.  + &lt;code&gt;Addresses&lt;/code&gt; &#x3D; null (optional, Addresses[]) ... List of addresses.     + &lt;code&gt;Members&lt;/code&gt;         + &lt;code&gt;AddressLine1&lt;/code&gt; &#x3D; null (optional, string) ... House number, street name and Unit number (i.e. 123 Q Street, Unit 102) or PO Box (i.e. 1821 Q Street).         + &lt;code&gt;AddressLine2&lt;/code&gt; &#x3D; null (optional, string) ... State or City and State or Zip (i.e. Sacramento, CA).  + &lt;code&gt;Phone&lt;/code&gt; &#x3D; null (optional, string) ... Phone number (formats: ###-###-####, (###) ###-####).  + &lt;code&gt;Email&lt;/code&gt; &#x3D; null (optional, string) ... E-mail address.

    :param galaxy_ap_name: e.g. Key
    :type galaxy_ap_name: str
    :param galaxy_ap_password: e.g. Secret
    :type galaxy_ap_password: str
    :param galaxy_search_type: e.g. DevAPIContactEnrich
    :type galaxy_search_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ContactEnrichPostRequest.from_dict(body)
    return web.Response(status=200)


async def email_enrich_post(request: web.Request, galaxy_ap_name=None, galaxy_ap_password=None, galaxy_search_type=None, body=None) -> web.Response:
    """Search

    ###### *Click on the grey search box above, to view sample request/response objects for Email Enrichment Search*  Perform a search:  1. Add your Access Profile username and password to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIEmailID  2.  Add search criteria to your request.     ~~~html             {                 \&quot;Email\&quot;:\&quot;johnsmith@somedomain\&quot;             }     ~~~  3.  Submit your search  The JSON request should have an email.  + &lt;code&gt;Email&lt;/code&gt; &#x3D; null (optional, string) ... E-mail address.

    :param galaxy_ap_name: e.g. Key
    :type galaxy_ap_name: str
    :param galaxy_ap_password: e.g. Secret
    :type galaxy_ap_password: str
    :param galaxy_search_type: e.g. DevAPIEmailID
    :type galaxy_search_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = EmailEnrichPostRequest.from_dict(body)
    return web.Response(status=200)


async def phone_enrich_post(request: web.Request, galaxy_ap_name=None, galaxy_ap_password=None, galaxy_search_type=None, body=None) -> web.Response:
    """Search

    ###### *Click on the grey search box above, to view sample request/response objects for Phone Enrichment Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPICallerID  2.  Add search criteria to your request.     ~~~html             {                 \&quot;Phone\&quot;:\&quot;(123) 456-7890\&quot;             }     ~~~  3.  Submit your search  The JSON request should have a phone number.  + &lt;code&gt;Phone&lt;/code&gt; &#x3D; null (optional, string) ... Phone number (formats: ###-###-####, (###) ###-####).

    :param galaxy_ap_name: e.g. Key
    :type galaxy_ap_name: str
    :param galaxy_ap_password: e.g. Secret
    :type galaxy_ap_password: str
    :param galaxy_search_type: e.g. DevAPICallerID
    :type galaxy_search_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PhoneEnrichPostRequest.from_dict(body)
    return web.Response(status=200)


async def search(request: web.Request, galaxy_ap_name=None, galaxy_ap_password=None, galaxy_search_type=None, body=None) -> web.Response:
    """Search

    ###### *Click on the grey search box above, to view sample request/response objects for the Identity Verification Search*  Perform a search:  1. Add your key and key secret to the request headers.     + galaxy-ap-name: [Key]     + galaxy-ap-password: [Secret]     + galaxy-search-type: DevAPIIDVerification  2.  Add search criteria to your request. At least two are required: SSN, Name, Phone, Address or Email.     ~~~html             {                 \&quot;FirstName\&quot;: \&quot;John\&quot;,                 \&quot;MiddleName\&quot;: \&quot;T\&quot;,                 \&quot;LastName\&quot;: \&quot;Lawrence\&quot;,                 \&quot;Dob\&quot;:\&quot;\&quot;,                 \&quot;Age\&quot;: 0,                 \&quot;Address\&quot;: {                     \&quot;addressLine1\&quot;:\&quot;123 Q Street, Unit 102\&quot;,                     \&quot;addressLine2\&quot;:\&quot;Sacramento, CA\&quot;                 },                 \&quot;PhoneNumber\&quot;:\&quot;\&quot;,                 \&quot;Email\&quot;:\&quot;\&quot;             }     ~~~  3.  Submit your search  A complete list of JSON request properties follows.  + &lt;code&gt;FirstName&lt;/code&gt;&#x3D; null (optional, string) ... First name.  + &lt;code&gt;MiddleName&lt;/code&gt; &#x3D; null (optional, string) ... Middle name or middle initial.  + &lt;code&gt;LastName&lt;/code&gt; &#x3D; null (optional, string) ... Last name.  + &lt;code&gt;Dob&lt;/code&gt; &#x3D; null (optional, string) ... Date of birth (format: MM/DD/YYYY).  + &lt;code&gt;Age&lt;/code&gt; &#x3D; null (optional, int) ... Age.  + &lt;code&gt;Addresses&lt;/code&gt; &#x3D; null (optional, Addresses[]) ... List of addresses.     + &lt;code&gt;Members&lt;/code&gt;         + &lt;code&gt;AddressLine1&lt;/code&gt; &#x3D; null (optional, string) ... House number, street name and Unit number (i.e. 123 Q Street, Unit 102) or PO Box (i.e. 1821 Q Street).         + &lt;code&gt;AddressLine2&lt;/code&gt; &#x3D; null (optional, string) ... State or City and State or Zip (i.e. Sacramento, CA).  + &lt;code&gt;Phone&lt;/code&gt; &#x3D; null (optional, string) ... Phone number (formats: ###-###-####, (###) ###-####).  + &lt;code&gt;Email&lt;/code&gt; &#x3D; null (optional, string) ... E-mail address.

    :param galaxy_ap_name: e.g. Key
    :type galaxy_ap_name: str
    :param galaxy_ap_password: e.g. Secret
    :type galaxy_ap_password: str
    :param galaxy_search_type: e.g. DevAPIIDVerification
    :type galaxy_search_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ContactEnrichPostRequest.from_dict(body)
    return web.Response(status=200)
