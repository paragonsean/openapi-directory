from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_post200_response import CheckPost200Response
from openapi_server.models.languages_get200_response_inner import LanguagesGet200ResponseInner
from openapi_server.models.words_add_post200_response import WordsAddPost200Response
from openapi_server.models.words_delete_post200_response import WordsDeletePost200Response
from openapi_server.models.words_get200_response import WordsGet200Response
from openapi_server import util


async def check_post(request: web.Request, language, text=None, data=None, username=None, api_key=None, dicts=None, mother_tongue=None, preferred_variants=None, enabled_rules=None, disabled_rules=None, enabled_categories=None, disabled_categories=None, enabled_only=None, level=None) -> web.Response:
    """Check a text

    The main feature - check a text with LanguageTool for possible style and grammar issues.

    :param language: A language code like &#x60;en-US&#x60;, &#x60;de-DE&#x60;, &#x60;fr&#x60;, or &#x60;auto&#x60; to guess the language automatically (see &#x60;preferredVariants&#x60; below). For languages with variants (English, German, Portuguese) spell checking will only be activated when you specify the variant, e.g. &#x60;en-GB&#x60; instead of just &#x60;en&#x60;.
    :type language: str
    :param text: The text to be checked. This or &#39;data&#39; is required.
    :type text: str
    :param data: The text to be checked, given as a JSON document that specifies what&#39;s text and what&#39;s markup. This or &#39;text&#39; is required. Markup will be ignored when looking for errors. Example text: &lt;pre&gt;A &amp;lt;b&gt;test&amp;lt;/b&gt;&lt;/pre&gt;JSON for the example text: &lt;pre&gt;{\\\&quot;annotation\\\&quot;:[  {\\\&quot;text\\\&quot;: \\\&quot;A \\\&quot;},  {\\\&quot;markup\\\&quot;: \\\&quot;&amp;lt;b&gt;\\\&quot;},  {\\\&quot;text\\\&quot;: \\\&quot;test\\\&quot;},  {\\\&quot;markup\\\&quot;: \\\&quot;&amp;lt;/b&gt;\\\&quot;} ]}&lt;/pre&gt; &lt;p&gt;If you have markup that should be interpreted as whitespace, like &lt;tt&gt;&amp;lt;p&amp;gt;&lt;/tt&gt; in HTML, you can have it interpreted like this: &lt;pre&gt;{\\\&quot;markup\\\&quot;: \\\&quot;&amp;lt;p&amp;gt;\\\&quot;, \\\&quot;interpretAs\\\&quot;: \\\&quot;\\\\n\\\\n\\\&quot;}&lt;/pre&gt;&lt;p&gt;The &#39;data&#39; feature is not limited to HTML or XML, it can be used for any kind of markup. Entities will need to be expanded in this input.
    :type data: str
    :param username: Set to get Premium API access: Your username/email as used to log in at languagetool.org.
    :type username: str
    :param api_key: Set to get Premium API access: &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;your API key&lt;/a&gt;
    :type api_key: str
    :param dicts: Comma-separated list of dictionaries to include words from; uses special default dictionary if this is unset
    :type dicts: str
    :param mother_tongue: A language code of the user&#39;s native language, enabling false friends checks for some language pairs.
    :type mother_tongue: str
    :param preferred_variants: Comma-separated list of preferred language variants. The language detector used with &#x60;language&#x3D;auto&#x60; can detect e.g. English, but it cannot decide whether British English or American English is used. Thus this parameter can be used to specify the preferred variants like &#x60;en-GB&#x60; and &#x60;de-AT&#x60;. Only available with &#x60;language&#x3D;auto&#x60;. You should set variants for at least German and English, as otherwise the spell checking will not work for those, as no spelling dictionary can be selected for just &#x60;en&#x60; or &#x60;de&#x60;.
    :type preferred_variants: str
    :param enabled_rules: IDs of rules to be enabled, comma-separated
    :type enabled_rules: str
    :param disabled_rules: IDs of rules to be disabled, comma-separated
    :type disabled_rules: str
    :param enabled_categories: IDs of categories to be enabled, comma-separated
    :type enabled_categories: str
    :param disabled_categories: IDs of categories to be disabled, comma-separated
    :type disabled_categories: str
    :param enabled_only: If true, only the rules and categories whose IDs are specified with &#x60;enabledRules&#x60; or &#x60;enabledCategories&#x60; are enabled.
    :type enabled_only: bool
    :param level: If set to &#x60;picky&#x60;, additional rules will be activated, i.e. rules that you might only find useful when checking formal text.
    :type level: str

    """
    return web.Response(status=200)


async def languages_get(request: web.Request, ) -> web.Response:
    """Get a list of supported languages.

    


    """
    return web.Response(status=200)


async def words_add_post(request: web.Request, word, username, api_key, dict=None) -> web.Response:
    """Add word to a dictionary

    Add a word to one of the user&#39;s personal dictionaries. Please note that this feature is considered to be used for personal dictionaries which must not contain more than 500 words. If this is an issue for you, please contact us.

    :param word: The word to be added. Must not be a phrase, i.e. cannot contain white space. The word is added to a global dictionary that applies to all languages.
    :type word: str
    :param username: Your username as used to log in at languagetool.org.
    :type username: str
    :param api_key: &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;Your API key&lt;/a&gt;
    :type api_key: str
    :param dict: Name of the dictionary to add the word to; non-existent dictionaries are created after calling this; if unset, adds to special default dictionary
    :type dict: str

    """
    return web.Response(status=200)


async def words_delete_post(request: web.Request, word, username, api_key, dict=None) -> web.Response:
    """Remove word from a dictionary

    Remove a word from one of the user&#39;s personal dictionaries.

    :param word: The word to be removed.
    :type word: str
    :param username: Your username as used to log in at languagetool.org.
    :type username: str
    :param api_key: &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;Your API key&lt;/a&gt;
    :type api_key: str
    :param dict: Name of the dictionary to remove the word from; if the dictionary is empty upon calling this, it is deleted; if unset, removes from special default dictionary
    :type dict: str

    """
    return web.Response(status=200)


async def words_get(request: web.Request, username, api_key, offset=None, limit=None, dicts=None) -> web.Response:
    """List words in dictionaries

    List words in the user&#39;s personal dictionaries.

    :param username: Your username as used to log in at languagetool.org.
    :type username: str
    :param api_key: &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;Your API key&lt;/a&gt;
    :type api_key: str
    :param offset: Offset of where to start in the list of words. Defaults to 0.
    :type offset: int
    :param limit: Maximum number of words to return. Defaults to 10.
    :type limit: int
    :param dicts: Comma-separated list of dictionaries to include words from; uses special default dictionary if this is unset
    :type dicts: str

    """
    return web.Response(status=200)
