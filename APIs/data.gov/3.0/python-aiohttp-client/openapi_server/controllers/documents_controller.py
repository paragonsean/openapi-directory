from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def document(request: web.Request, response_format, document_id=None, federal_register_number=None) -> web.Response:
    """Returns Document information

    

    :param response_format: Format
    :type response_format: str
    :param document_id: FDMS Document ID
    :type document_id: str
    :param federal_register_number: Federal Register Document Number
    :type federal_register_number: str

    """
    return web.Response(status=200)


async def documents(request: web.Request, response_format, counts_only=None, encoded=None, s=None, dct=None, dktid=None, dkt=None, cp=None, a=None, rpp=None, po=None, cs=None, np=None, cmsd=None, cmd=None, crd=None, rd=None, pd=None, cat=None, sb=None, so=None, dktst=None, dktst2=None, docst=None) -> web.Response:
    """Search for Documents

    This API allows users to build a query based on any of the parameters below.  If you have trouble building queries, you may wish to try them through the &lt;a href&#x3D;\&quot;http://www.regulations.gov/#!advancedSearch\&quot;&gt;Advanced Search&lt;/a&gt; page on the Regulations.gov website.

    :param response_format: Format
    :type response_format: str
    :param counts_only: Counts Only: &lt;ul&gt;&lt;li&gt;1 (will return only the document count for a search query)&lt;/li&gt;&lt;li&gt;0 (will return documents as well)&lt;/li&gt;&lt;/ul&gt;
    :type counts_only: int
    :param encoded: Encoded: &lt;ul&gt;&lt;li&gt;1 (will accept Regulations.gov style encoded parameters)&lt;/li&gt;&lt;li&gt;0 (will not accept such encoded parameters)&lt;/li&gt;&lt;/ul&gt;
    :type encoded: int
    :param s: Keyword(s)
    :type s: str
    :param dct: Document Type: &lt;ul&gt;&lt;li&gt;N: Notice&lt;/li&gt;&lt;li&gt;PR: Proposed Rule&lt;/li&gt;&lt;li&gt;FR: Rule&lt;/li&gt;&lt;li&gt;O: Other&lt;/li&gt;&lt;li&gt;SR: Supporting &amp; Related Material&lt;/li&gt;&lt;li&gt;PS: Public Submission&lt;/li&gt;&lt;/ul&gt;
    :type dct: str
    :param dktid: Valid Docket ID (ex. SEC-2012-0044)
    :type dktid: str
    :param dkt: Docket Type: &lt;ul&gt;&lt;li&gt;R: Rulemaking&lt;/li&gt;&lt;li&gt;N: Nonrulemaking&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;A Docket Type is either Rulemaking or Nonrulemaking. A Rulemaking docket includes the type of regulation that establishes a rule. While a Non-Rulemaking docket does not include a rule.&lt;/p&gt;
    :type dkt: str
    :param cp: Comment Period: &lt;ul&gt;&lt;li&gt;O: Open&lt;/li&gt;&lt;li&gt;C: Closed&lt;/li&gt;&lt;/ul&gt;
    :type cp: str
    :param a: Federal Agency: List of accepted Federal Agency values. This field allows multiple values. Ex. a&#x3D;FMCSA%252BEPA%252BFDA
    :type a: str
    :param rpp: Results Per Page 10, 25, 100, 500, 1,000.  Results per page may not exceed 1,000.
    :type rpp: str
    :param po: Enter the page offset (always starts with 0). This is used in conjunction with results per page to provide large data sets. For example, if a search produces 82 results and the result per page is set to 25, this will generate 4 pages. 3 pages will have 25 results and the last page will have 7 results. Page offset values for each page will be: &lt;pre&gt;Page 1: po&#x3D;0 Page 2: po&#x3D;25 Page 3: po&#x3D;50 Page 4: po&#x3D;75&lt;/pre&gt; The total number of pages is [total results/results per page] and page offset for page X is [X-1 * results per page]
    :type po: int
    :param cs: Comment Period Closing Soon: &lt;ul&gt;&lt;li&gt;0 (closing today)&lt;/li&gt;&lt;li&gt;3 (closing within 3 days)&lt;/li&gt;&lt;li&gt;15 (closing within 15 days)&lt;/li&gt;&lt;li&gt;30 (closing within 30 days)&lt;/li&gt;&lt;li&gt;90 (closing within 90 days)&lt;/li&gt;&lt;/ul&gt;
    :type cs: int
    :param np: Newly Posted: &lt;ul&gt;&lt;li&gt;0 (posted today)&lt;/li&gt;&lt;li&gt;3 (posted within last 3 days)&lt;/li&gt;&lt;li&gt;15 (posted within last 15 days)&lt;/li&gt;&lt;li&gt;30 (posted within last 30 days)&lt;/li&gt;&lt;li&gt;90 (posted within last 90 days)&lt;/li&gt;&lt;/ul&gt;  For periods of time beyond 90-days, please use a date range with the Posted Date parameter.
    :type np: int
    :param cmsd: Comment Period Start Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period End Date is also provided, then ensure the Comment Period Start date is earlier.
    :type cmsd: str
    :param cmd: Comment Period End Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period Start Date is also provided, then ensure the Comment Period End date is after.&lt;br/&gt;* Comment Period Start and End Dates are mutually exclusive with the &#39;closing soon&#39; parameter. If both are provided, &#39;closing soon&#39; will be ignored.
    :type cmd: str
    :param crd: Creation Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;crd&#x3D;11/06/13-03/06/14&lt;/code&gt;
    :type crd: str
    :param rd: Received Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;rd&#x3D;11/06/13-03/06/14&lt;/code&gt;
    :type rd: str
    :param pd: Posted Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;pd&#x3D;11/06/13-03/06/14&lt;/code&gt;
    :type pd: str
    :param cat: Document Category: &lt;ul&gt;&lt;li&gt;AD (Aerospace and Transportation)&lt;/li&gt; &lt;li&gt;AEP (Agriculture, Environment, and Public Lands)&lt;/li&gt; &lt;li&gt;BFS (Banking and Financial)&lt;/li&gt; &lt;li&gt;CT (Commerce and International)&lt;/li&gt; &lt;li&gt;LES (Defense, Law Enforcement, and Security)&lt;/li&gt; &lt;li&gt;EELS (Education, Labor, Presidential, and Government Services)&lt;/li&gt; &lt;li&gt;EUMM (Energy, Natural Resources, and Utilities)&lt;/li&gt; &lt;li&gt;HCFP (Food Safety, Health, and Pharmaceutical)&lt;/li&gt; &lt;li&gt;PRE (Housing, Development, and Real Estate)&lt;/li&gt; &lt;li&gt;ITT (Technology and Telecommunications)&lt;/li&gt;&lt;/ul&gt;
    :type cat: str
    :param sb: Sort By: &lt;ul&gt;&lt;li&gt;docketId (Docket ID)&lt;/li&gt;&lt;li&gt;docId (Document ID)&lt;/li&gt;&lt;li&gt;title (Title)&lt;/li&gt;&lt;li&gt;postedDate (Posted Date)&lt;/li&gt;&lt;li&gt;agency (Agency)&lt;/li&gt;&lt;li&gt;documentType (Document Type)&lt;/li&gt;&lt;li&gt;submitterName (Submitter Name)&lt;/li&gt;&lt;li&gt;organization (Organization)&lt;/li&gt;&lt;/ul&gt; Sort Order is REQUIRED if this parameter is included.
    :type sb: str
    :param so: Sort Order: &lt;ul&gt;&lt;li&gt;ASC: Ascending&lt;/li&gt;&lt;li&gt;DESC: Descending&lt;/li&gt;&lt;/ul&gt;
    :type so: str
    :param dktst: Docket Subtype: Only one docket subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned.
    :type dktst: str
    :param dktst2: Docket Sub-subtype: Only one docket sub-subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned.
    :type dktst2: str
    :param docst: Document Subtype: Single or multiple document subtypes may be included.  Multiple values should be passed as follows: &lt;code&gt;docst&#x3D;%20Certificate+of+Service%252BCorrespondence&lt;/code&gt;
    :type docst: str

    """
    cmsd = util.deserialize_date(cmsd)
    cmd = util.deserialize_date(cmd)
    crd = util.deserialize_date(crd)
    rd = util.deserialize_date(rd)
    pd = util.deserialize_date(pd)
    return web.Response(status=200)
