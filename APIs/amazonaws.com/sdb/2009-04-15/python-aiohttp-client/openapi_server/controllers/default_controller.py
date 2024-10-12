from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_does_not_exist import AttributeDoesNotExist
from openapi_server.models.batch_delete_attributes_request import BatchDeleteAttributesRequest
from openapi_server.models.batch_put_attributes_request import BatchPutAttributesRequest
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.delete_attributes_request import DeleteAttributesRequest
from openapi_server.models.delete_domain_request import DeleteDomainRequest
from openapi_server.models.domain_metadata_request import DomainMetadataRequest
from openapi_server.models.domain_metadata_result import DomainMetadataResult
from openapi_server.models.get_batch_delete_attributes_items_parameter_inner import GETBatchDeleteAttributesItemsParameterInner
from openapi_server.models.get_batch_put_attributes_items_parameter_inner import GETBatchPutAttributesItemsParameterInner
from openapi_server.models.get_delete_attributes_attributes_parameter_inner import GETDeleteAttributesAttributesParameterInner
from openapi_server.models.get_delete_attributes_expected_parameter import GETDeleteAttributesExpectedParameter
from openapi_server.models.get_put_attributes_attributes_parameter_inner import GETPutAttributesAttributesParameterInner
from openapi_server.models.get_attributes_request import GetAttributesRequest
from openapi_server.models.get_attributes_result import GetAttributesResult
from openapi_server.models.invalid_next_token import InvalidNextToken
from openapi_server.models.list_domains_request import ListDomainsRequest
from openapi_server.models.list_domains_result import ListDomainsResult
from openapi_server.models.missing_parameter import MissingParameter
from openapi_server.models.no_such_domain import NoSuchDomain
from openapi_server.models.number_domains_exceeded import NumberDomainsExceeded
from openapi_server.models.number_item_attributes_exceeded import NumberItemAttributesExceeded
from openapi_server.models.number_submitted_attributes_exceeded import NumberSubmittedAttributesExceeded
from openapi_server.models.put_attributes_request import PutAttributesRequest
from openapi_server.models.request_timeout import RequestTimeout
from openapi_server.models.select_request import SelectRequest
from openapi_server.models.select_result import SelectResult
from openapi_server.models.too_many_requested_attributes import TooManyRequestedAttributes
from openapi_server import util


async def g_et_batch_delete_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, items, action, version) -> web.Response:
    """g_et_batch_delete_attributes

    &lt;p&gt; Performs multiple DeleteAttributes operations in a single call, which reduces round trips and latencies. This enables Amazon SimpleDB to optimize requests, which generally yields better throughput. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you specify BatchDeleteAttributes without attributes or values, all the attributes for the item are deleted. &lt;/p&gt; &lt;p&gt; BatchDeleteAttributes is an idempotent operation; running it multiple times on the same item or attribute doesn&#39;t result in an error. &lt;/p&gt; &lt;p&gt; The BatchDeleteAttributes operation succeeds or fails in its entirety. There are no partial deletes. You can execute multiple BatchDeleteAttributes operations and other operations in parallel. However, large numbers of concurrent BatchDeleteAttributes calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. &lt;/p&gt; &lt;p&gt; This operation does not support conditions using Expected.X.Name, Expected.X.Value, or Expected.X.Exists. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;25 item limit per BatchDeleteAttributes operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain in which the attributes are being deleted.
    :type domain_name: str
    :param items: A list of items on which to perform the operation.
    :type items: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str

    """
    items = [GETBatchDeleteAttributesItemsParameterInner.from_dict(d) for d in items]
    return web.Response(status=200)


async def g_et_batch_put_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, items, action, version) -> web.Response:
    """g_et_batch_put_attributes

    &lt;p&gt; The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation creates or replaces attributes within one or more items. By using this operation, the client can perform multiple &lt;a&gt;PutAttribute&lt;/a&gt; operation with a single call. This helps yield savings in round trips and latencies, enabling Amazon SimpleDB to optimize requests and generally produce better throughput. &lt;/p&gt; &lt;p&gt; The client may specify the item name with the &lt;code&gt;Item.X.ItemName&lt;/code&gt; parameter. The client may specify new attributes using a combination of the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; parameters. The client may specify the first attribute for the first item using the parameters &lt;code&gt;Item.0.Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.0.Value&lt;/code&gt;, and for the second attribute for the first item by the parameters &lt;code&gt;Item.0.Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified within an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requester can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual value. Setting this value to &lt;code&gt;true&lt;/code&gt; will cause the new attribute values to replace the existing attribute values. For example, if an item &lt;code&gt;I&lt;/code&gt; has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }, { &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requester does a BatchPutAttributes of &lt;code&gt;{&#39;I&#39;, &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the Replace parameter set to true, the final attributes of the item will be &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, replacing the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; You cannot specify an empty string as an item or as an attribute name. The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation succeeds or fails in its entirety. There are no partial puts. &lt;/note&gt; &lt;important&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. This operation does not support conditions using &lt;code&gt;Expected.X.Name&lt;/code&gt;, &lt;code&gt;Expected.X.Value&lt;/code&gt;, or &lt;code&gt;Expected.X.Exists&lt;/code&gt;. &lt;/important&gt; &lt;p&gt; You can execute multiple &lt;code&gt;BatchPutAttributes&lt;/code&gt; operations and other operations in parallel. However, large numbers of concurrent &lt;code&gt;BatchPutAttributes&lt;/code&gt; calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;1 billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;li&gt;25 item limit per &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain in which the attributes are being stored.
    :type domain_name: str
    :param items: A list of items on which to perform the operation.
    :type items: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str

    """
    items = [GETBatchPutAttributesItemsParameterInner.from_dict(d) for d in items]
    return web.Response(status=200)


async def g_et_create_domain(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, action, version) -> web.Response:
    """g_et_create_domain

    &lt;p&gt; The &lt;code&gt;CreateDomain&lt;/code&gt; operation creates a new domain. The domain name should be unique among the domains associated with the Access Key ID provided in the request. The &lt;code&gt;CreateDomain&lt;/code&gt; operation may take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; CreateDomain is an idempotent operation; running it multiple times using the same domain name will not result in an error response. &lt;/note&gt; &lt;p&gt; The client can create up to 100 domains per account. &lt;/p&gt; &lt;p&gt; If the client requires additional domains, go to &lt;a href&#x3D;\&quot;http://aws.amazon.com/contact-us/simpledb-limit-request/\&quot;&gt; http://aws.amazon.com/contact-us/simpledb-limit-request/&lt;/a&gt;. &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain to create. The name can range between 3 and 255 characters and can contain the following characters: a-z, A-Z, 0-9, &#39;_&#39;, &#39;-&#39;, and &#39;.&#39;.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def g_et_delete_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, item_name, action, version, attributes=None, expected=None) -> web.Response:
    """g_et_delete_attributes

    &lt;p&gt; Deletes one or more attributes associated with an item. If all attributes of the item are deleted, the item is deleted. &lt;/p&gt; &lt;note&gt; If &lt;code&gt;DeleteAttributes&lt;/code&gt; is called without being passed any attributes or values specified, all the attributes for the item are deleted. &lt;/note&gt; &lt;p&gt; &lt;code&gt;DeleteAttributes&lt;/code&gt; is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of item data and uses an eventual consistency update model, performing a &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;code&gt;DeleteAttributes&lt;/code&gt; or &lt;a&gt;PutAttributes&lt;/a&gt; operation (write) might not return updated item data. &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain in which to perform the operation.
    :type domain_name: str
    :param item_name: The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs.
    :type item_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param attributes: A list of Attributes. Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items.
    :type attributes: list | bytes
    :param expected: The update condition which, if specified, determines whether the specified attributes will be deleted or not. The update condition must be satisfied in order for this request to be processed and the attributes to be deleted.
    :type expected: dict | bytes

    """
    attributes = [GETDeleteAttributesAttributesParameterInner.from_dict(d) for d in attributes]
    expected = .from_dict(expected)
    return web.Response(status=200)


async def g_et_delete_domain(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, action, version) -> web.Response:
    """g_et_delete_domain

    &lt;p&gt; The &lt;code&gt;DeleteDomain&lt;/code&gt; operation deletes a domain. Any items (and their attributes) in the domain are deleted as well. The &lt;code&gt;DeleteDomain&lt;/code&gt; operation might take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; Running &lt;code&gt;DeleteDomain&lt;/code&gt; on a domain that does not exist or running the function multiple times using the same domain name will not result in an error response. &lt;/note&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain to delete.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def g_et_domain_metadata(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, action, version) -> web.Response:
    """g_et_domain_metadata

     Returns information about the domain, including when the domain was created, the number of items and attributes in the domain, and the size of the attribute names and values. 

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain for which to display the metadata of.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def g_et_get_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, item_name, action, version, attribute_names=None, consistent_read=None) -> web.Response:
    """g_et_get_attributes

    &lt;p&gt; Returns all of the attributes associated with the specified item. Optionally, the attributes returned can be limited to one or more attributes by specifying an attribute name parameter. &lt;/p&gt; &lt;p&gt; If the item does not exist on the replica that was accessed for this operation, an empty set is returned. The system does not return an error as it cannot guarantee the item does not exist on other replicas. &lt;/p&gt; &lt;note&gt; If GetAttributes is called without being passed any attribute names, all the attributes for the item are returned. &lt;/note&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain in which to perform the operation.
    :type domain_name: str
    :param item_name: The name of the item.
    :type item_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param attribute_names: The names of the attributes.
    :type attribute_names: List[]
    :param consistent_read: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If &lt;code&gt;true&lt;/code&gt;, any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
    :type consistent_read: bool

    """
    return web.Response(status=200)


async def g_et_list_domains(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, max_number_of_domains=None, next_token=None) -> web.Response:
    """g_et_list_domains

     The &lt;code&gt;ListDomains&lt;/code&gt; operation lists all domains associated with the Access Key ID. It returns domain names up to the limit set by &lt;a href&#x3D;\&quot;#MaxNumberOfDomains\&quot;&gt;MaxNumberOfDomains&lt;/a&gt;. A &lt;a href&#x3D;\&quot;#NextToken\&quot;&gt;NextToken&lt;/a&gt; is returned if there are more than &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; domains. Calling &lt;code&gt;ListDomains&lt;/code&gt; successive times with the &lt;code&gt;NextToken&lt;/code&gt; provided by the operation returns up to &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; more domain names with each successive operation call. 

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param max_number_of_domains: The maximum number of domain names you want returned. The range is 1 to 100. The default setting is 100.
    :type max_number_of_domains: int
    :param next_token: A string informing Amazon SimpleDB where to start the next list of domain names.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_put_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, domain_name, item_name, attributes, action, version, expected=None) -> web.Response:
    """g_et_put_attributes

    &lt;p&gt; The PutAttributes operation creates or replaces attributes in an item. The client may specify new attributes using a combination of the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; parameters. The client specifies the first attribute by the parameters &lt;code&gt;Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Attribute.0.Value&lt;/code&gt;, the second attribute by the parameters &lt;code&gt;Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified in an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requestor can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual attribute. Setting this value to &lt;code&gt;true&lt;/code&gt; causes the new attribute value to replace the existing attribute value(s). For example, if an item has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt;, &lt;code&gt;{ &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requestor calls &lt;code&gt;PutAttributes&lt;/code&gt; using the attributes &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the &lt;code&gt;Replace&lt;/code&gt; parameter set to true, the final attributes of the item are changed to &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, which replaces the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; Using &lt;code&gt;PutAttributes&lt;/code&gt; to replace attribute values that do not exist will not result in an error response. &lt;/note&gt; &lt;p&gt; You cannot specify an empty string as an attribute name. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of client data and uses an eventual consistency update model, an immediate &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;a&gt;PutAttributes&lt;/a&gt; or &lt;a&gt;DeleteAttributes&lt;/a&gt; operation (write) might not return the updated data. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 total attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;One billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param domain_name: The name of the domain in which to perform the operation.
    :type domain_name: str
    :param item_name: The name of the item.
    :type item_name: str
    :param attributes: The list of attributes.
    :type attributes: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param expected: The update condition which, if specified, determines whether the specified attributes will be updated or not. The update condition must be satisfied in order for this request to be processed and the attributes to be updated.
    :type expected: dict | bytes

    """
    attributes = [GETPutAttributesAttributesParameterInner.from_dict(d) for d in attributes]
    expected = .from_dict(expected)
    return web.Response(status=200)


async def g_et_select(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, select_expression, action, version, next_token=None, consistent_read=None) -> web.Response:
    """g_et_select

    &lt;p&gt; The &lt;code&gt;Select&lt;/code&gt; operation returns a set of attributes for &lt;code&gt;ItemNames&lt;/code&gt; that match the select expression. &lt;code&gt;Select&lt;/code&gt; is similar to the standard SQL SELECT statement. &lt;/p&gt; &lt;p&gt; The total size of the response cannot exceed 1 MB in total size. Amazon SimpleDB automatically adjusts the number of items returned per page to enforce this limit. For example, if the client asks to retrieve 2500 items, but each individual item is 10 kB in size, the system returns 100 items and an appropriate &lt;code&gt;NextToken&lt;/code&gt; so the client can access the next page of results. &lt;/p&gt; &lt;p&gt; For information on how to construct select expressions, see Using Select to Create Amazon SimpleDB Queries in the Developer Guide. &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param select_expression: The expression used to query the domain.
    :type select_expression: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param next_token: A string informing Amazon SimpleDB where to start the next list of &lt;code&gt;ItemNames&lt;/code&gt;.
    :type next_token: str
    :param consistent_read: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If &lt;code&gt;true&lt;/code&gt;, any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
    :type consistent_read: bool

    """
    return web.Response(status=200)


async def p_ost_batch_delete_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_batch_delete_attributes

    &lt;p&gt; Performs multiple DeleteAttributes operations in a single call, which reduces round trips and latencies. This enables Amazon SimpleDB to optimize requests, which generally yields better throughput. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you specify BatchDeleteAttributes without attributes or values, all the attributes for the item are deleted. &lt;/p&gt; &lt;p&gt; BatchDeleteAttributes is an idempotent operation; running it multiple times on the same item or attribute doesn&#39;t result in an error. &lt;/p&gt; &lt;p&gt; The BatchDeleteAttributes operation succeeds or fails in its entirety. There are no partial deletes. You can execute multiple BatchDeleteAttributes operations and other operations in parallel. However, large numbers of concurrent BatchDeleteAttributes calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. &lt;/p&gt; &lt;p&gt; This operation does not support conditions using Expected.X.Name, Expected.X.Value, or Expected.X.Exists. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;25 item limit per BatchDeleteAttributes operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = BatchDeleteAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_batch_put_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_batch_put_attributes

    &lt;p&gt; The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation creates or replaces attributes within one or more items. By using this operation, the client can perform multiple &lt;a&gt;PutAttribute&lt;/a&gt; operation with a single call. This helps yield savings in round trips and latencies, enabling Amazon SimpleDB to optimize requests and generally produce better throughput. &lt;/p&gt; &lt;p&gt; The client may specify the item name with the &lt;code&gt;Item.X.ItemName&lt;/code&gt; parameter. The client may specify new attributes using a combination of the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; parameters. The client may specify the first attribute for the first item using the parameters &lt;code&gt;Item.0.Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.0.Value&lt;/code&gt;, and for the second attribute for the first item by the parameters &lt;code&gt;Item.0.Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified within an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requester can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual value. Setting this value to &lt;code&gt;true&lt;/code&gt; will cause the new attribute values to replace the existing attribute values. For example, if an item &lt;code&gt;I&lt;/code&gt; has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }, { &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requester does a BatchPutAttributes of &lt;code&gt;{&#39;I&#39;, &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the Replace parameter set to true, the final attributes of the item will be &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, replacing the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; You cannot specify an empty string as an item or as an attribute name. The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation succeeds or fails in its entirety. There are no partial puts. &lt;/note&gt; &lt;important&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. This operation does not support conditions using &lt;code&gt;Expected.X.Name&lt;/code&gt;, &lt;code&gt;Expected.X.Value&lt;/code&gt;, or &lt;code&gt;Expected.X.Exists&lt;/code&gt;. &lt;/important&gt; &lt;p&gt; You can execute multiple &lt;code&gt;BatchPutAttributes&lt;/code&gt; operations and other operations in parallel. However, large numbers of concurrent &lt;code&gt;BatchPutAttributes&lt;/code&gt; calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;1 billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;li&gt;25 item limit per &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = BatchPutAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_domain(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_create_domain

    &lt;p&gt; The &lt;code&gt;CreateDomain&lt;/code&gt; operation creates a new domain. The domain name should be unique among the domains associated with the Access Key ID provided in the request. The &lt;code&gt;CreateDomain&lt;/code&gt; operation may take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; CreateDomain is an idempotent operation; running it multiple times using the same domain name will not result in an error response. &lt;/note&gt; &lt;p&gt; The client can create up to 100 domains per account. &lt;/p&gt; &lt;p&gt; If the client requires additional domains, go to &lt;a href&#x3D;\&quot;http://aws.amazon.com/contact-us/simpledb-limit-request/\&quot;&gt; http://aws.amazon.com/contact-us/simpledb-limit-request/&lt;/a&gt;. &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDomainRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_delete_attributes

    &lt;p&gt; Deletes one or more attributes associated with an item. If all attributes of the item are deleted, the item is deleted. &lt;/p&gt; &lt;note&gt; If &lt;code&gt;DeleteAttributes&lt;/code&gt; is called without being passed any attributes or values specified, all the attributes for the item are deleted. &lt;/note&gt; &lt;p&gt; &lt;code&gt;DeleteAttributes&lt;/code&gt; is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of item data and uses an eventual consistency update model, performing a &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;code&gt;DeleteAttributes&lt;/code&gt; or &lt;a&gt;PutAttributes&lt;/a&gt; operation (write) might not return updated item data. &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_domain(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_delete_domain

    &lt;p&gt; The &lt;code&gt;DeleteDomain&lt;/code&gt; operation deletes a domain. Any items (and their attributes) in the domain are deleted as well. The &lt;code&gt;DeleteDomain&lt;/code&gt; operation might take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; Running &lt;code&gt;DeleteDomain&lt;/code&gt; on a domain that does not exist or running the function multiple times using the same domain name will not result in an error response. &lt;/note&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteDomainRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_domain_metadata(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_domain_metadata

     Returns information about the domain, including when the domain was created, the number of items and attributes in the domain, and the size of the attribute names and values. 

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = DomainMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_get_attributes

    &lt;p&gt; Returns all of the attributes associated with the specified item. Optionally, the attributes returned can be limited to one or more attributes by specifying an attribute name parameter. &lt;/p&gt; &lt;p&gt; If the item does not exist on the replica that was accessed for this operation, an empty set is returned. The system does not return an error as it cannot guarantee the item does not exist on other replicas. &lt;/p&gt; &lt;note&gt; If GetAttributes is called without being passed any attribute names, all the attributes for the item are returned. &lt;/note&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_domains(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, max_number_of_domains=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_domains

     The &lt;code&gt;ListDomains&lt;/code&gt; operation lists all domains associated with the Access Key ID. It returns domain names up to the limit set by &lt;a href&#x3D;\&quot;#MaxNumberOfDomains\&quot;&gt;MaxNumberOfDomains&lt;/a&gt;. A &lt;a href&#x3D;\&quot;#NextToken\&quot;&gt;NextToken&lt;/a&gt; is returned if there are more than &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; domains. Calling &lt;code&gt;ListDomains&lt;/code&gt; successive times with the &lt;code&gt;NextToken&lt;/code&gt; provided by the operation returns up to &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; more domain names with each successive operation call. 

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param max_number_of_domains: Pagination limit
    :type max_number_of_domains: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListDomainsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_attributes(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, body=None) -> web.Response:
    """p_ost_put_attributes

    &lt;p&gt; The PutAttributes operation creates or replaces attributes in an item. The client may specify new attributes using a combination of the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; parameters. The client specifies the first attribute by the parameters &lt;code&gt;Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Attribute.0.Value&lt;/code&gt;, the second attribute by the parameters &lt;code&gt;Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified in an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requestor can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual attribute. Setting this value to &lt;code&gt;true&lt;/code&gt; causes the new attribute value to replace the existing attribute value(s). For example, if an item has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt;, &lt;code&gt;{ &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requestor calls &lt;code&gt;PutAttributes&lt;/code&gt; using the attributes &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the &lt;code&gt;Replace&lt;/code&gt; parameter set to true, the final attributes of the item are changed to &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, which replaces the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; Using &lt;code&gt;PutAttributes&lt;/code&gt; to replace attribute values that do not exist will not result in an error response. &lt;/note&gt; &lt;p&gt; You cannot specify an empty string as an attribute name. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of client data and uses an eventual consistency update model, an immediate &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;a&gt;PutAttributes&lt;/a&gt; or &lt;a&gt;DeleteAttributes&lt;/a&gt; operation (write) might not return the updated data. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 total attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;One billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_select(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, action, version, next_token=None, body=None) -> web.Response:
    """p_ost_select

    &lt;p&gt; The &lt;code&gt;Select&lt;/code&gt; operation returns a set of attributes for &lt;code&gt;ItemNames&lt;/code&gt; that match the select expression. &lt;code&gt;Select&lt;/code&gt; is similar to the standard SQL SELECT statement. &lt;/p&gt; &lt;p&gt; The total size of the response cannot exceed 1 MB in total size. Amazon SimpleDB automatically adjusts the number of items returned per page to enforce this limit. For example, if the client asks to retrieve 2500 items, but each individual item is 10 kB in size, the system returns 100 items and an appropriate &lt;code&gt;NextToken&lt;/code&gt; so the client can access the next page of results. &lt;/p&gt; &lt;p&gt; For information on how to construct select expressions, see Using Select to Create Amazon SimpleDB Queries in the Developer Guide. &lt;/p&gt;

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SelectRequest.from_dict(body)
    return web.Response(status=200)
