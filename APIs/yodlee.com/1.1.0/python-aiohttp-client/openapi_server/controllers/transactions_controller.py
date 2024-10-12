from typing import List, Dict
from aiohttp import web

from openapi_server.models.transaction_categorization_rule import TransactionCategorizationRule
from openapi_server.models.transaction_categorization_rule_request import TransactionCategorizationRuleRequest
from openapi_server.models.transaction_categorization_rule_response import TransactionCategorizationRuleResponse
from openapi_server.models.transaction_category_request import TransactionCategoryRequest
from openapi_server.models.transaction_category_response import TransactionCategoryResponse
from openapi_server.models.transaction_count_response import TransactionCountResponse
from openapi_server.models.transaction_request import TransactionRequest
from openapi_server.models.transaction_response import TransactionResponse
from openapi_server.models.update_category_request import UpdateCategoryRequest
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def create_or_run_transaction_categorization_rules(request: web.Request, action=None, rule_param=None) -> web.Response:
    """Create or Run Transaction Categorization Rule

    The Create or Run Transaction Categorization Rule endpoint is used to: &lt;br&gt;Create transaction categorization rules for both system and user-defined categories.&lt;br&gt;Run all the transaction categorization rules to categorize transactions by calling the endpoint with action&#x3D;run as the query parameter. &lt;br&gt;&lt;br&gt;The input body parameters to create transaction categorization rules follow:&lt;br&gt;     categoryId - This field is mandatory and numeric&lt;br&gt;     priority - This field is optional and numeric. Priority decides the order in which the rule gets applied on transactions.&lt;br&gt;     ruleClause - This field is mandatory and should contain at least one rule&lt;br&gt;     field - The value can be description or amount&lt;br&gt;&lt;br&gt;       If the field value is description then,&lt;br&gt;         1. operation - value can be stringEquals or stringContains&lt;br&gt;         2. value - value should be min of 3 and max of 50 characters&lt;br&gt;&lt;br&gt;       If the field value is amount then, &lt;br&gt;         1. operation - value can be numberEquals, numberLessThan, numberLessThanEquals, numberGreaterThan or numberGreaterThanEquals&lt;br&gt;         2. value - min value 0 and a max value of 99999999999.99 is allowed&lt;br&gt;The HTTP response code is 201 (Created Successfully).

    :param action: To run rules, pass action&#x3D;run. Only value run is supported
    :type action: str
    :param rule_param: rules(JSON format) to categorize the transactions
    :type rule_param: str

    """
    return web.Response(status=200)


async def create_transaction_category(request: web.Request, body) -> web.Response:
    """Create Category

    The create transaction categories service is used to create user-defined categories for a system-defined category.&lt;br&gt;The parentCategoryId is the system-defined category id.This can be retrieved using get transaction categories service.&lt;br&gt;The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.&lt;br&gt;The HTTP response code is 201 (Created successfully).&lt;br&gt;

    :param body: User Transaction Category in JSON format
    :type body: dict | bytes

    """
    body = TransactionCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def delete_transaction_categorization_rule(request: web.Request, rule_id) -> web.Response:
    """Delete Transaction Categorization Rule

    The delete transaction categorization rule service is used to delete the given user-defined transaction categorization rule for both system-defined category as well as user-defined category.&lt;br&gt;This will delete all the corresponding rule clauses associated with the rule.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

    :param rule_id: ruleId
    :type rule_id: int

    """
    return web.Response(status=200)


async def delete_transaction_category(request: web.Request, category_id) -> web.Response:
    """Delete Category

    The delete transaction categories service is used to delete the given user-defined category.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

    :param category_id: categoryId
    :type category_id: int

    """
    return web.Response(status=200)


async def get_transaction_categories(request: web.Request, ) -> web.Response:
    """Get Transaction Category List

    The categories service returns the list of available transaction categories.&lt;br&gt;High level category is returned in the response only if it is opted by the customer.&lt;br&gt;When invoked by passing the cobrand session or admin access token, this service returns the supported transaction categories at the cobrand level. &lt;br&gt;When invoked by passing the cobrand session and the user session or user access token, this service returns the transaction categories &lt;br&gt;along with user-defined categories.&lt;br&gt;Double quotes in the user-defined category name will be prefixed by backslashes (&amp;#92;) in the response, &lt;br&gt;e.g. Toys \&quot;R\&quot; Us.&lt;br/&gt;Source and id are the primary attributes of the category entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;


    """
    return web.Response(status=200)


async def get_transaction_categorization_rules(request: web.Request, ) -> web.Response:
    """Get Transaction Categorization Rules

    The get transaction categorization rule service is used to get all the categorization rules.&lt;br&gt;


    """
    return web.Response(status=200)


async def get_transaction_categorization_rules_deprecated(request: web.Request, ) -> web.Response:
    """Get Transaction Categorization Rules

    The get transaction categorization rule service is used to get all the categorization rules.&lt;br&gt;


    """
    return web.Response(status=200)


async def get_transactions(request: web.Request, account_id=None, base_type=None, category_id=None, category_type=None, container=None, detail_category_id=None, from_date=None, high_level_category_id=None, keyword=None, skip=None, to_date=None, top=None, type=None) -> web.Response:
    """Get Transactions

    The Transaction service is used to get a list of transactions for a user.&lt;br&gt;By default, this service returns the last 30 days of transactions from today&#39;s date.&lt;br&gt;The keyword parameter performs a contains search on the original, consumer, and simple description attributes, replace the special characters #, &amp;, and + with percent-encoding values %23, %26, and %2B respectively. Eg: for -Debit# , pass the input as -Debit%23.&lt;br&gt;Values for categoryId parameter can be fetched from get transaction category list service.&lt;br&gt; The categoryId is used to filter transactions based on system-defined category as well as user-defined category.&lt;br&gt;User-defined categoryIds should be provided in the filter with the prefix &#39;&#39;U&#39;&#39;. E.g. U10002&lt;br&gt;The skip and top parameters are used for pagination. In the skip and top parameters pass the number of records to be skipped and retrieved, respectively. The response header provides the links to retrieve the next and previous set of transactions.&lt;br&gt;Double quotes in the merchant name will be prefixed by backslashes (&amp;#92;) in the response, e.g. Toys \&quot;R\&quot; Us. &lt;br&gt;sourceId is a unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts. Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;&lt;li&gt; &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/Transaction_Data_Enrichment\&quot;&gt;TDE&lt;/a&gt; is made available for bank and card accounts and for the US market only.The address field in the response is available only when the TDE key is turned on.&lt;li&gt;The pagination feature is available by default. If no values are passed in the skip and top parameters, the API will only return the first 500 transactions.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;br&gt;

    :param account_id: Comma separated accountIds
    :type account_id: str
    :param base_type: DEBIT/CREDIT
    :type base_type: str
    :param category_id: Comma separated categoryIds
    :type category_id: str
    :param category_type: Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION)
    :type category_type: str
    :param container: bank/creditCard/investment/insurance/loan
    :type container: str
    :param detail_category_id: Comma separated detailCategoryIds
    :type detail_category_id: str
    :param from_date: Transaction from date(YYYY-MM-DD)
    :type from_date: str
    :param high_level_category_id: Comma separated highLevelCategoryIds
    :type high_level_category_id: str
    :param keyword: Transaction search text
    :type keyword: str
    :param skip: skip (Min 0)
    :type skip: int
    :param to_date: Transaction end date (YYYY-MM-DD)
    :type to_date: str
    :param top: top (Max 500)
    :type top: int
    :param type: Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment
    :type type: str

    """
    return web.Response(status=200)


async def get_transactions_count(request: web.Request, account_id=None, base_type=None, category_id=None, category_type=None, container=None, detail_category_id=None, from_date=None, high_level_category_id=None, keyword=None, to_date=None, type=None) -> web.Response:
    """Get Transactions Count

    The count service provides the total number of transactions for a specific user depending on the input parameters passed.&lt;br&gt;If you are implementing pagination for transactions, call this endpoint before calling GET /transactions to know the number of transactions that are returned for the input parameters passed.&lt;br&gt;The functionality of the input parameters remains the same as that of the GET /transactions endpoint.&lt;br&gt;

    :param account_id: Comma separated accountIds 
    :type account_id: str
    :param base_type: DEBIT/CREDIT
    :type base_type: str
    :param category_id: Comma separated categoryIds
    :type category_id: str
    :param category_type: Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION)
    :type category_type: str
    :param container: bank/creditCard/investment/insurance/loan
    :type container: str
    :param detail_category_id: Comma separated detailCategoryIds
    :type detail_category_id: str
    :param from_date: Transaction from date(YYYY-MM-DD)
    :type from_date: str
    :param high_level_category_id: Comma separated highLevelCategoryIds
    :type high_level_category_id: str
    :param keyword: Transaction search text 
    :type keyword: str
    :param to_date: Transaction end date (YYYY-MM-DD)
    :type to_date: str
    :param type: Transaction Type(SELL,SWEEP, etc.)
    :type type: str

    """
    return web.Response(status=200)


async def run_transaction_categorization_rule(request: web.Request, action, rule_id) -> web.Response:
    """Run Transaction Categorization Rule

    The run transaction categorization rule service is used to run a rule on transactions, to categorize the transactions.&lt;br&gt;The HTTP response code is 204 (Success with no content).&lt;br&gt;

    :param action: 
    :type action: str
    :param rule_id: Unique id of the categorization rule
    :type rule_id: int

    """
    return web.Response(status=200)


async def update_transaction(request: web.Request, transaction_id, body) -> web.Response:
    """Update Transaction

    The update transaction service is used to update the category,consumer description, memo for a transaction.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

    :param transaction_id: transactionId
    :type transaction_id: int
    :param body: transactionRequest
    :type body: dict | bytes

    """
    body = TransactionRequest.from_dict(body)
    return web.Response(status=200)


async def update_transaction_categorization_rule(request: web.Request, rule_id, body) -> web.Response:
    """Update Transaction Categorization Rule

    The update transaction categorization rule service is used to update a categorization rule for both system-defined category as well as user-defined category.&lt;br&gt;ruleParam JSON input should be as explained in the create transaction categorization rule service.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

    :param rule_id: ruleId
    :type rule_id: int
    :param body: transactionCategoriesRuleRequest
    :type body: dict | bytes

    """
    body = TransactionCategorizationRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_transaction_category(request: web.Request, body) -> web.Response:
    """Update Category

    The update transaction categories service is used to update the transaction category name&lt;br&gt;for a high level category, a system-defined category and a user-defined category.&lt;br&gt;The renamed category can be set back to the original name by passing an empty string for categoryName.&lt;br&gt;The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

    :param body: updateCategoryRequest
    :type body: dict | bytes

    """
    body = UpdateCategoryRequest.from_dict(body)
    return web.Response(status=200)
