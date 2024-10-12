from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_document_request import AnalyzeDocumentRequest
from openapi_server.models.analyze_document_response import AnalyzeDocumentResponse
from openapi_server.models.analyze_expense_request import AnalyzeExpenseRequest
from openapi_server.models.analyze_expense_response import AnalyzeExpenseResponse
from openapi_server.models.analyze_id_request import AnalyzeIDRequest
from openapi_server.models.analyze_id_response import AnalyzeIDResponse
from openapi_server.models.detect_document_text_request import DetectDocumentTextRequest
from openapi_server.models.detect_document_text_response import DetectDocumentTextResponse
from openapi_server.models.get_document_analysis_request import GetDocumentAnalysisRequest
from openapi_server.models.get_document_analysis_response import GetDocumentAnalysisResponse
from openapi_server.models.get_document_text_detection_request import GetDocumentTextDetectionRequest
from openapi_server.models.get_document_text_detection_response import GetDocumentTextDetectionResponse
from openapi_server.models.get_expense_analysis_request import GetExpenseAnalysisRequest
from openapi_server.models.get_expense_analysis_response import GetExpenseAnalysisResponse
from openapi_server.models.get_lending_analysis_request import GetLendingAnalysisRequest
from openapi_server.models.get_lending_analysis_response import GetLendingAnalysisResponse
from openapi_server.models.get_lending_analysis_summary_request import GetLendingAnalysisSummaryRequest
from openapi_server.models.get_lending_analysis_summary_response import GetLendingAnalysisSummaryResponse
from openapi_server.models.start_document_analysis_request import StartDocumentAnalysisRequest
from openapi_server.models.start_document_analysis_response import StartDocumentAnalysisResponse
from openapi_server.models.start_document_text_detection_request import StartDocumentTextDetectionRequest
from openapi_server.models.start_document_text_detection_response import StartDocumentTextDetectionResponse
from openapi_server.models.start_expense_analysis_request import StartExpenseAnalysisRequest
from openapi_server.models.start_expense_analysis_response import StartExpenseAnalysisResponse
from openapi_server.models.start_lending_analysis_request import StartLendingAnalysisRequest
from openapi_server.models.start_lending_analysis_response import StartLendingAnalysisResponse
from openapi_server import util


async def analyze_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """analyze_document

    &lt;p&gt;Analyzes an input document for relationships between detected items. &lt;/p&gt; &lt;p&gt;The types of information returned are as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Form data (key-value pairs). The related information is returned in two &lt;a&gt;Block&lt;/a&gt; objects, each of type &lt;code&gt;KEY_VALUE_SET&lt;/code&gt;: a KEY &lt;code&gt;Block&lt;/code&gt; object and a VALUE &lt;code&gt;Block&lt;/code&gt; object. For example, &lt;i&gt;Name: Ana Silva Carolina&lt;/i&gt; contains a key and value. &lt;i&gt;Name:&lt;/i&gt; is the key. &lt;i&gt;Ana Silva Carolina&lt;/i&gt; is the value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Table and table cell data. A TABLE &lt;code&gt;Block&lt;/code&gt; object contains information about a detected table. A CELL &lt;code&gt;Block&lt;/code&gt; object is returned for each cell in a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lines and words of text. A LINE &lt;code&gt;Block&lt;/code&gt; object contains one or more WORD &lt;code&gt;Block&lt;/code&gt; objects. All lines and words that are detected in the document are returned (including text that doesn&#39;t have a relationship with the value of &lt;code&gt;FeatureTypes&lt;/code&gt;). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Signatures. A SIGNATURE &lt;code&gt;Block&lt;/code&gt; object contains the location information of a signature in a document. If used in conjunction with forms or tables, a signature can be given a Key-Value pairing or be detected in the cell of a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query Result. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT &lt;code&gt;Block&lt;/code&gt; object contains information about a selection element, including the selection status.&lt;/p&gt; &lt;p&gt;You can choose which type of analysis to perform by specifying the &lt;code&gt;FeatureTypes&lt;/code&gt; list. &lt;/p&gt; &lt;p&gt;The output is returned in a list of &lt;code&gt;Block&lt;/code&gt; objects.&lt;/p&gt; &lt;p&gt; &lt;code&gt;AnalyzeDocument&lt;/code&gt; is a synchronous operation. To analyze documents asynchronously, use &lt;a&gt;StartDocumentAnalysis&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AnalyzeDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def analyze_expense(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """analyze_expense

    &lt;p&gt; &lt;code&gt;AnalyzeExpense&lt;/code&gt; synchronously analyzes an input document for financially related relationships between text.&lt;/p&gt; &lt;p&gt;Information is returned as &lt;code&gt;ExpenseDocuments&lt;/code&gt; and seperated as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LineItemGroups&lt;/code&gt;- A data set containing &lt;code&gt;LineItems&lt;/code&gt; which store information about the lines of text, such as an item purchased and its price on a receipt.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SummaryFields&lt;/code&gt;- Contains all other information a receipt, such as header information or the vendors name.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AnalyzeExpenseRequest.from_dict(body)
    return web.Response(status=200)


async def analyze_id(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """analyze_id

    Analyzes identity documents for relevant information. This information is extracted and returned as &lt;code&gt;IdentityDocumentFields&lt;/code&gt;, which records both the normalized field and value of the extracted text. Unlike other Amazon Textract operations, &lt;code&gt;AnalyzeID&lt;/code&gt; doesn&#39;t return any Geometry data.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AnalyzeIDRequest.from_dict(body)
    return web.Response(status=200)


async def detect_document_text(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detect_document_text

    &lt;p&gt;Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be in one of the following image formats: JPEG, PNG, PDF, or TIFF. &lt;code&gt;DetectDocumentText&lt;/code&gt; returns the detected text in an array of &lt;a&gt;Block&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;Each document page has as an associated &lt;code&gt;Block&lt;/code&gt; of type PAGE. Each PAGE &lt;code&gt;Block&lt;/code&gt; object is the parent of LINE &lt;code&gt;Block&lt;/code&gt; objects that represent the lines of detected text on a page. A LINE &lt;code&gt;Block&lt;/code&gt; object is a parent for each word that makes up the line. Words are represented by &lt;code&gt;Block&lt;/code&gt; objects of type WORD.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectDocumentText&lt;/code&gt; is a synchronous operation. To analyze documents asynchronously, use &lt;a&gt;StartDocumentTextDetection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DetectDocumentTextRequest.from_dict(body)
    return web.Response(status=200)


async def get_document_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_document_analysis

    &lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.&lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;a&gt;StartDocumentAnalysis&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDocumentAnalysis&lt;/code&gt; returns an array of &lt;a&gt;Block&lt;/a&gt; objects. The following types of information are returned: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Form data (key-value pairs). The related information is returned in two &lt;a&gt;Block&lt;/a&gt; objects, each of type &lt;code&gt;KEY_VALUE_SET&lt;/code&gt;: a KEY &lt;code&gt;Block&lt;/code&gt; object and a VALUE &lt;code&gt;Block&lt;/code&gt; object. For example, &lt;i&gt;Name: Ana Silva Carolina&lt;/i&gt; contains a key and value. &lt;i&gt;Name:&lt;/i&gt; is the key. &lt;i&gt;Ana Silva Carolina&lt;/i&gt; is the value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Table and table cell data. A TABLE &lt;code&gt;Block&lt;/code&gt; object contains information about a detected table. A CELL &lt;code&gt;Block&lt;/code&gt; object is returned for each cell in a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lines and words of text. A LINE &lt;code&gt;Block&lt;/code&gt; object contains one or more WORD &lt;code&gt;Block&lt;/code&gt; objects. All lines and words that are detected in the document are returned (including text that doesn&#39;t have a relationship with the value of the &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; &lt;code&gt;FeatureTypes&lt;/code&gt; input parameter). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query Results. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;While processing a document with queries, look out for &lt;code&gt;INVALID_REQUEST_PARAMETERS&lt;/code&gt; output. This indicates that either the per page query limit has been exceeded or that the operation is trying to query a page in the document which doesn’t exist. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT &lt;code&gt;Block&lt;/code&gt; object contains information about a selection element, including the selection status.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDocumentAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def get_document_text_detection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_document_text_detection

    &lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.&lt;/p&gt; &lt;p&gt;You start asynchronous text detection by calling &lt;a&gt;StartDocumentTextDetection&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDocumentTextDetection&lt;/code&gt; returns an array of &lt;a&gt;Block&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;Each document page has as an associated &lt;code&gt;Block&lt;/code&gt; of type PAGE. Each PAGE &lt;code&gt;Block&lt;/code&gt; object is the parent of LINE &lt;code&gt;Block&lt;/code&gt; objects that represent the lines of detected text on a page. A LINE &lt;code&gt;Block&lt;/code&gt; object is a parent for each word that makes up the line. Words are represented by &lt;code&gt;Block&lt;/code&gt; objects of type WORD.&lt;/p&gt; &lt;p&gt;Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDocumentTextDetectionRequest.from_dict(body)
    return web.Response(status=200)


async def get_expense_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_expense_analysis

    &lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes invoices and receipts. Amazon Textract finds contact information, items purchased, and vendor name, from input invoices and receipts.&lt;/p&gt; &lt;p&gt;You start asynchronous invoice/receipt analysis by calling &lt;a&gt;StartExpenseAnalysis&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). Upon completion of the invoice/receipt analysis, Amazon Textract publishes the completion status to the Amazon Simple Notification Service (Amazon SNS) topic. This topic must be registered in the initial call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;. To get the results of the invoice/receipt analysis operation, first ensure that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html\&quot;&gt;Analyzing Invoices and Receipts&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetExpenseAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def get_lending_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_lending_analysis

    &lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes text in a lending document. &lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;code&gt;StartLendingAnalysis&lt;/code&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetLendingAnalysis, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetLendingAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def get_lending_analysis_summary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_lending_analysis_summary

    &lt;p&gt;Gets summarized results for the &lt;code&gt;StartLendingAnalysis&lt;/code&gt; operation, which analyzes text in a lending document. The returned summary consists of information about documents grouped together by a common document type. Information like detected signatures, page numbers, and split documents is returned with respect to the type of grouped document. &lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;code&gt;StartLendingAnalysis&lt;/code&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call &lt;code&gt;GetLendingAnalysisSummary&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetLendingAnalysisSummaryRequest.from_dict(body)
    return web.Response(status=200)


async def start_document_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_document_analysis

    &lt;p&gt;Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use &lt;a&gt;DocumentLocation&lt;/a&gt; to specify the bucket name and file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetDocumentAnalysis&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartDocumentAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def start_document_text_detection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_document_text_detection

    &lt;p&gt;Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentTextDetection&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use &lt;a&gt;DocumentLocation&lt;/a&gt; to specify the bucket name and file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartTextDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When text detection is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetDocumentTextDetection&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartDocumentTextDetectionRequest.from_dict(body)
    return web.Response(status=200)


async def start_expense_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_expense_analysis

    &lt;p&gt;Starts the asynchronous analysis of invoices or receipts for data like contact information, items purchased, and vendor names.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExpenseAnalysis&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, and PDF format. The documents must be stored in an Amazon S3 bucket. Use the &lt;a&gt;DocumentLocation&lt;/a&gt; parameter to specify the name of your S3 bucket and the name of the document in that bucket. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExpenseAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you will provide to &lt;code&gt;GetExpenseAnalysis&lt;/code&gt; to retrieve the results of the operation. When the analysis of the input invoices/receipts is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you provide to the &lt;code&gt;NotificationChannel&lt;/code&gt;. To obtain the results of the invoice and receipt analysis operation, ensure that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetExpenseAnalysis&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) that was returned by your call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/invoice-receipts.html\&quot;&gt;Analyzing Invoices and Receipts&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartExpenseAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def start_lending_analysis(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_lending_analysis

    &lt;p&gt;Starts the classification and analysis of an input document. &lt;code&gt;StartLendingAnalysis&lt;/code&gt; initiates the classification and analysis of a packet of lending documents. &lt;code&gt;StartLendingAnalysis&lt;/code&gt; operates on a document file located in an Amazon S3 bucket.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLendingAnalysis&lt;/code&gt; can analyze text in documents that are in one of the following formats: JPEG, PNG, TIFF, PDF. Use &lt;code&gt;DocumentLocation&lt;/code&gt; to specify the bucket name and the file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLendingAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When the text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If the status is SUCCEEDED you can call either &lt;code&gt;GetLendingAnalysis&lt;/code&gt; or &lt;code&gt;GetLendingAnalysisSummary&lt;/code&gt; and provide the &lt;code&gt;JobId&lt;/code&gt; to obtain the results of the analysis.&lt;/p&gt; &lt;p&gt;If using &lt;code&gt;OutputConfig&lt;/code&gt; to specify an Amazon S3 bucket, the output will be contained within the specified prefix in a directory labeled with the job-id. In the directory there are 3 sub-directories: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;detailedResponse (contains the GetLendingAnalysis response)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;summaryResponse (for the GetLendingAnalysisSummary response)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;splitDocuments (documents split across logical boundaries)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartLendingAnalysisRequest.from_dict(body)
    return web.Response(status=200)
