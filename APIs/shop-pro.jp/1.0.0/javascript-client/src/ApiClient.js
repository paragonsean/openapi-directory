/**
 * カラーミーショップアプリストア API
 * # カラーミーショップアプリストア API  [アプリストア](https://app.shop-pro.jp/)にて公開するアプリに対して、一般公開している[カラーミーショップAPI](https://developer.shop-pro.jp/docs/colorme-api)に加えて、カラーミーショップアプリストアAPI（以下、アプリストアAPIといいます）を利用することが出来ます。アプリストアAPIでは以下のことが行えます。 - 課金データ(アプリ内課金、従量課金)の作成 - インラインスクリプトタグの取得・作成・更新・削除 - スクリプトタグの取得・作成・更新・削除  ## 利用手順  アプリストアAPIを利用するには、OAuth認証が必要です。OAuth認証の基本的な流れについては[カラーミーショップAPIドキュメント](https://developer.shop-pro.jp/docs/colorme-api)を参照してください。 アプリストアAPIの利用のために、以下のscopeが追加で指定可能になります。[カラーミーショップAPIドキュメント](https://developer.shop-pro.jp/docs/colorme-api)に掲載されているscopeと合わせてご利用ください。  |スコープ|機能| |---|---| |`write_application_charge`|課金データの作成| |`read_shop_script_tags`|ショップページのスクリプトタグを参照| |`write_shop_script_tags`|ショップページへスクリプトタグを追加・更新| |`read_inline_script_tags`|インラインスクリプトタグを参照| |`write_inline_script_tags`|インラインスクリプトタグを追加・更新| |`read_script_tags`|スクリプトタグを参照(deprecated)| |`write_script_tags`|スクリプトタグを追加・更新(deprecated)|  (例) カラーミーショップアカウントの認証ページを表示 ``` https://api.shop-pro.jp/oauth/authorize?client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&response_type=code&scope=read_products%20write_products%20write_application_charge ```  ## 課金設定 料金プラン（月額課金・従量課金・買い切り）による課金や、アプリ内課金をご利用いただくにはアプリごとに課金設定の登録が必要です。 この設定は [カラーミーショップ デベロッパー](https://developer.shop-pro.jp) から行うことができます。  登録できる課金形式やその使い方の詳細については[アプリストア 開発ガイドのアプリ課金のページ](https://developer.shop-pro.jp/getting-started/appstore-billing/)をご覧ください  ## アプリのインストール ショップオーナーがアプリをインストールしたとき、以下の処理をカラーミーショップが行います。 - 選択された料金プランに基づき課金開始 - インストールフックの呼び出し  ### インストールフック アプリのインストール時に、インストールに関する情報を `POST` メソッド、 `application/json` 形式で通知します。 通知先のURLは[カラーミーショップ デベロッパー](https://developer.shop-pro.jp/)にログインし、各アプリストア アプリのアプリ設定から登録を行ってください。  以下のパラメータが送信されます。課金請求に必要なパラメータを含みますので、必ず受け取れるようにしてください。  |パラメータ|機能|形式| |---|---|---| |`account_id`|インストールしたショップオーナーのアカウントID|PA+8桁の整数| |`application_charge_source_id`|プラン課金ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`recurring_application_charge_id`|（買い切り以外の課金の場合）課金契約ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`application_charge_id`|（買い切りの場合）課金契約ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`trial_term`|（無料お試し期間がある場合）無料お試し期間|JSONオブジェクト| |`mail`|ショップオーナーへの連絡メールアドレス|文字列|  `application_charge_source_id` はデベロッパーサイトで設定したプラン課金のIDです。インストールされた料金プランの判別にご利用いただけます。  `recurring_application_charge_id` と `application_charge_id` はインストールごとに発行されるユニークなIDです。ショップオーナーが一度アンインストールした後に、再度同じショップオーナーがアプリのインストールを行った際には新たに別のIDが発行されます。  `recurring_application_charge_id` は「買い切り」以外の課金である「無料」「月額」「月額＋従量」「月額＋初期費用」「従量のみ」のプラン課金のインストールの際に発行されます。  従量による課金を伴うプラン課金の場合は、従量分の料金を請求する際に 課金契約ID(`recurring_application_charge_id`) が必要になるので、必ず記録するようにしてください。  `mail` パラメータの値はショップオーナーへの連絡手段としてご利用いただけます。インストール後に認可フローが中断され、アクセストークンが得られない際のショップオーナーへの連絡手段としてご活用いただけます。このパラメータはカラーミーショップの非公開情報として登録されている値です。左記以外の用途でこの値をアプリの機能で使用しないでください。  例) 買い切りの場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"F3RN9A\",   \"application_charge_id\": \"A3FT4N\",   \"mail\": \"shop@example.com\" } ```  例) 月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"F3RN9A\",   \"recurring_application_charge_id\": \"A3FT4N\",   \"mail\": \"shop@example.com\" } ```  無料お試し期間を設定した課金の場合、以下の情報を `trial_term` パラメータとして送信します。 無料お試し期間中は従量課金APIを呼び出して課金請求することはできません。  |パラメータ|機能|形式| |---|---|---| |`starts_at`|無料お試し開始日時|整数値(UNIXタイムスタンプ)| |`ends_at`|無料お試し終了日時|整数値(UNIXタイムスタンプ)|  例) 無料お試し期間がある月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"F3RN9A\",   \"recurring_application_charge_id\": \"A3FT4N\",   \"mail\": \"shop@example.com\",   \"trial_term\" {     \"starts_at\": 1565017200,     \"ends_at\": 1567609200   } } ```  受け取りに成功した場合は、以下のパラメータを `application/json` 形式でレスポンスボディに付与し、 ステータスコード `200` レスポンスをカラーミーショップへ返却してください。 ステータスコード `200` レスポンスをカラーミーショップが受け取れない場合、もしくは以下のパラメーターが返却されなかった場合、インストールを中止し、インストールによって発生した情報は破棄されます。  |パラメータ|機能|形式| |---|---|---| |`redirect_url`|インストール成功後に遷移するURL|文字列（URL）|  例) ``` {   \"redirect_url\": \"https://example.com\" } ``` インストール完了後、インストールフックのレスポンスパラメータの `redirect_url` へ画面遷移しますので、APIを利用する場合は `redirect_url` より先の画面でOAuth認証の実装をお願いします。  ## アプリのアンインストール ショップオーナーがアプリをアンインストールしたとき、以下の処理をカラーミーショップが行います。 - OAuth認証のアクセストークンの無効化 - 登録したインラインスクリプトタグ・スクリプトタグの削除 - 月額課金形式の場合、継続課金の無効化  ### アンインストールフック アンインストール直後に `POST` メソッドで、以下の情報を `application/json` 形式で通知します。 通知先のURLは[カラーミーショップ デベロッパー](https://developer.shop-pro.jp/)にログインし、各アプリストア アプリのアプリ設定から登録を行ってください。  ※ [アンインストールAPI](#operation/deleteInstallation)のご利用によるアンインストール時はアンインストールフックは通知されません。  受け取りに成功した場合はステータスコード `200` のレスポンスを返却してください。  |パラメータ|機能|形式| |---|---|---| |`account_id`|アンインストールしたショップオーナーのアカウントID|PA+8桁の整数| |`application_charge_source_id`|プラン課金ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`uninstalled_at`|アンインストール日時|整数値(UNIXタイムスタンプ)| |`reason`|アンインストール理由| `by_shop_owner` (ショップオーナーによる)<br /> `by_unpaid` (未払いによる) | |`recurring_application_charge_id`|（買い切り以外の課金の場合）課金契約ID|数字と大文字アルファベットで構成される文字列(6桁以上)| |`usage_charge`|（従量課金の場合）従量課金アンインストール情報|JSONオブジェクト|  アンインストールフックの通知が伴うアンインストールは以下の操作のいずれかによって行われます。アンインストールの理由を `reason` パラメータで確認できます。  |reasonパラメータの値|アンインストール理由| |---|---| |`by_shop_owner`|ショップオーナーによるアンインストール操作| |`by_unpaid`|ポイント不足による利用料徴収の失敗による自動アンインストール|  課金契約ID `recurring_application_charge_id` はインストールフックで通知したIDと同じIDが通知されます。  料金プランが従量課金の場合、アンインストール後に従量課金データの作成を可能にするために、以下の情報を `usage_charge` パラメータとして送信します。 アンインストール後はOAuthのアクセストークンが無効化されているため、アクセストークンを利用して従量課金APIを呼び出すことができなくなります。 アンインストール後はアクセストークンの代わりに `api_token` をリクエストヘッダーに含め、従量課金APIを呼び出してください。 無料お試し期間中にアプリがアンインストールされた場合は、`api_token` は発行されません。 詳しくは、[従量課金データの作成](https://app.shop-pro.jp/open_api#operation/createUsageCharge)を参照してください。 `api_token` を利用した従量課金APIの呼び出しは、ポイント締め日 `closing_on` までとなっておりますので、ご注意ください。  |パラメータ|機能|形式| |---|---|---| |`api_token`|アンインストール後に従量課金APIを利用いただくために必要な情報|文字列| |`closing_on`|ポイント締め日|整数値(UNIXタイムスタンプ)|  通常、 `closing_on` は、アンインストール直前まで利用されていた契約の期間の月末となります。以下に例を示します。  |アンインストール日|直前まで利用されていた契約の期間|closing_on の示す日時| |---|---|---| |2021/01/09|2021/12/10〜2021/01/09|2021/01/31| |2021/01/10|2021/01/10〜2021/02/09|2021/02/28|  従量課金の場合のユーザーの契約期間については[こちら](https://shop-pro.jp/manual/appstore_fee)をご参照ください  アンインストールフックの例を以下に示します。  例) 買い切りの場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"Q21GPC\",   \"uninstalled_at\": 1552022739,   \"reason\": \"by_shop_owner\" } ```  例) 月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"EW3V21\",   \"recurring_application_charge_id\": \"F3RN9A\",   \"uninstalled_at\": 1552022740,   \"reason\": \"by_shop_owner\" } ```  例) 従量課金を含む月額課金の場合 ``` {   \"account_id\": \"PA00000001\",   \"application_charge_source_id\": \"WA37CA\",   \"recurring_application_charge_id\": \"F3WQ1S\",   \"uninstalled_at\": 1552022740,   \"reason\": \"by_shop_owner\",   \"usage_charge\": {     \"api_token\": \"token\",     \"closing_on\": 1552533465   } } ```  ### アンインストールフックのリトライ ステータスコード `200` のレスポンスをカラーミーショップが受け取れない場合は、ステータスコード `200` をカラーミーショップが受け取るまで、以下の条件で再度アンインストール情報を送信します。 なお、カラーミーショップによるアンインストール処理は、アンインストールフックの送信結果の成否によらず、アンインストールが実行されたときに完了します。  - 2時間30分ごとにアンインストールフックの仕様に基づき再送します - 最大で合計19回再送します - すべての再送の試行でステータスコード `200` をカラーミーショップが受け取れない場合は、公認デベロッパー申請時に登録されたメールアドレス宛にメールを送信します  ## インストール・アンインストールフックの署名検証 `X-Appstore-Signature` リクエストヘッダーに含まれる署名を検証して、リクエストがカラーミーショップから送信されたことを確認することを推奨します。  検証の手順は以下のとおりです。  1. カラーミーショップが発行した `webhook_secret` を秘密鍵として、HMAC-SHA256アルゴリズムを使用してリクエストボディのダイジェスト値を取得します。 2. ダイジェスト値をBase64エンコードした値とリクエストヘッダーに付与された署名( `X-Appstore-Signature` の値）が一致することを確認します。   サンプルコード(ruby) ```ruby WEBHOOK_SECRET = 'my_webhook_secret'  payload_body = request.body.read signature = Base64.strict_encode64(OpenSSL::HMAC.digest('sha256', WEBHOOK_SECRET, payload_body)) ActiveSupport::SecurityUtils.secure_compare(signature, request.env['HTTP_X_APPSTORE_SIGNATURE']) ```  ### 発信元IPアドレスについて  発信元IPアドレスは固定ではありません。そのためIPアドレスが固定されていることを前提としてアプリケーションを開発しないでください。  インストールフックおよびアンインストールフックのリクエストの発信元を検証する場合は上記の署名検証を行なってください。 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import superagent from "superagent";
import querystring from "querystring";

/**
* @module ApiClient
* @version 1.0.0
*/

/**
* Manages low level client-server communications, parameter marshalling, etc. There should not be any need for an
* application to use this class directly - the *Api and model classes provide the public API for the service. The
* contents of this file should be regarded as internal but are documented for completeness.
* @alias module:ApiClient
* @class
*/
class ApiClient {
    /**
     * The base URL against which to resolve every API call's (relative) path.
     * Overrides the default value set in spec file if present
     * @param {String} basePath
     */
    constructor(basePath = 'https://api.shop-pro.jp') {
        /**
         * The base URL against which to resolve every API call's (relative) path.
         * @type {String}
         * @default https://api.shop-pro.jp
         */
        this.basePath = basePath.replace(/\/+$/, '');

        /**
         * The authentication methods to be included for all API calls.
         * @type {Array.<String>}
         */
        this.authentications = {
            'OAuth2': {type: 'oauth2'}
        }

        /**
         * The default HTTP headers to be included for all API calls.
         * @type {Array.<String>}
         * @default {}
         */
        this.defaultHeaders = {
            'User-Agent': 'OpenAPI-Generator/1.0.0/Javascript'
        };

        /**
         * The default HTTP timeout for all API calls.
         * @type {Number}
         * @default 60000
         */
        this.timeout = 60000;

        /**
         * If set to false an additional timestamp parameter is added to all API GET calls to
         * prevent browser caching
         * @type {Boolean}
         * @default true
         */
        this.cache = true;

        /**
         * If set to true, the client will save the cookies from each server
         * response, and return them in the next request.
         * @default false
         */
        this.enableCookies = false;

        /*
         * Used to save and return cookies in a node.js (non-browser) setting,
         * if this.enableCookies is set to true.
         */
        if (typeof window === 'undefined') {
          this.agent = new superagent.agent();
        }

        /*
         * Allow user to override superagent agent
         */
         this.requestAgent = null;

        /*
         * Allow user to add superagent plugins
         */
        this.plugins = null;

    }

    /**
    * Returns a string representation for an actual parameter.
    * @param param The actual parameter.
    * @returns {String} The string representation of <code>param</code>.
    */
    paramToString(param) {
        if (param == undefined || param == null) {
            return '';
        }
        if (param instanceof Date) {
            return param.toJSON();
        }
        if (ApiClient.canBeJsonified(param)) {
            return JSON.stringify(param);
        }

        return param.toString();
    }

    /**
    * Returns a boolean indicating if the parameter could be JSON.stringified
    * @param param The actual parameter
    * @returns {Boolean} Flag indicating if <code>param</code> can be JSON.stringified
    */
    static canBeJsonified(str) {
        if (typeof str !== 'string' && typeof str !== 'object') return false;
        try {
            const type = str.toString();
            return type === '[object Object]'
                || type === '[object Array]';
        } catch (err) {
            return false;
        }
    };

   /**
    * Builds full URL by appending the given path to the base URL and replacing path parameter place-holders with parameter values.
    * NOTE: query parameters are not handled here.
    * @param {String} path The path to append to the base URL.
    * @param {Object} pathParams The parameter values to append.
    * @param {String} apiBasePath Base path defined in the path, operation level to override the default one
    * @returns {String} The encoded path with parameter values substituted.
    */
    buildUrl(path, pathParams, apiBasePath) {
        if (!path.match(/^\//)) {
            path = '/' + path;
        }

        var url = this.basePath + path;

        // use API (operation, path) base path if defined
        if (apiBasePath !== null && apiBasePath !== undefined) {
            url = apiBasePath + path;
        }

        url = url.replace(/\{([\w-\.#]+)\}/g, (fullMatch, key) => {
            var value;
            if (pathParams.hasOwnProperty(key)) {
                value = this.paramToString(pathParams[key]);
            } else {
                value = fullMatch;
            }

            return encodeURIComponent(value);
        });

        return url;
    }

    /**
    * Checks whether the given content type represents JSON.<br>
    * JSON content type examples:<br>
    * <ul>
    * <li>application/json</li>
    * <li>application/json; charset=UTF8</li>
    * <li>APPLICATION/JSON</li>
    * </ul>
    * @param {String} contentType The MIME content type to check.
    * @returns {Boolean} <code>true</code> if <code>contentType</code> represents JSON, otherwise <code>false</code>.
    */
    isJsonMime(contentType) {
        return Boolean(contentType != null && contentType.match(/^application\/json(;.*)?$/i));
    }

    /**
    * Chooses a content type from the given array, with JSON preferred; i.e. return JSON if included, otherwise return the first.
    * @param {Array.<String>} contentTypes
    * @returns {String} The chosen content type, preferring JSON.
    */
    jsonPreferredMime(contentTypes) {
        for (var i = 0; i < contentTypes.length; i++) {
            if (this.isJsonMime(contentTypes[i])) {
                return contentTypes[i];
            }
        }

        return contentTypes[0];
    }

    /**
    * Checks whether the given parameter value represents file-like content.
    * @param param The parameter to check.
    * @returns {Boolean} <code>true</code> if <code>param</code> represents a file.
    */
    isFileParam(param) {
        // fs.ReadStream in Node.js and Electron (but not in runtime like browserify)
        if (typeof require === 'function') {
            let fs;
            try {
                fs = require('fs');
            } catch (err) {}
            if (fs && fs.ReadStream && param instanceof fs.ReadStream) {
                return true;
            }
        }

        // Buffer in Node.js
        if (typeof Buffer === 'function' && param instanceof Buffer) {
            return true;
        }

        // Blob in browser
        if (typeof Blob === 'function' && param instanceof Blob) {
            return true;
        }

        // File in browser (it seems File object is also instance of Blob, but keep this for safe)
        if (typeof File === 'function' && param instanceof File) {
            return true;
        }

        return false;
    }

    /**
    * Normalizes parameter values:
    * <ul>
    * <li>remove nils</li>
    * <li>keep files and arrays</li>
    * <li>format to string with `paramToString` for other cases</li>
    * </ul>
    * @param {Object.<String, Object>} params The parameters as object properties.
    * @returns {Object.<String, Object>} normalized parameters.
    */
    normalizeParams(params) {
        var newParams = {};
        for (var key in params) {
            if (params.hasOwnProperty(key) && params[key] != undefined && params[key] != null) {
                var value = params[key];
                if (this.isFileParam(value) || Array.isArray(value)) {
                    newParams[key] = value;
                } else {
                    newParams[key] = this.paramToString(value);
                }
            }
        }

        return newParams;
    }

    /**
    * Builds a string representation of an array-type actual parameter, according to the given collection format.
    * @param {Array} param An array parameter.
    * @param {module:ApiClient.CollectionFormatEnum} collectionFormat The array element separator strategy.
    * @returns {String|Array} A string representation of the supplied collection, using the specified delimiter. Returns
    * <code>param</code> as is if <code>collectionFormat</code> is <code>multi</code>.
    */
    buildCollectionParam(param, collectionFormat) {
        if (param == null) {
            return null;
        }
        switch (collectionFormat) {
            case 'csv':
                return param.map(this.paramToString, this).join(',');
            case 'ssv':
                return param.map(this.paramToString, this).join(' ');
            case 'tsv':
                return param.map(this.paramToString, this).join('\t');
            case 'pipes':
                return param.map(this.paramToString, this).join('|');
            case 'multi':
                //return the array directly as SuperAgent will handle it as expected
                return param.map(this.paramToString, this);
            case 'passthrough':
                return param;
            default:
                throw new Error('Unknown collection format: ' + collectionFormat);
        }
    }

    /**
    * Applies authentication headers to the request.
    * @param {Object} request The request object created by a <code>superagent()</code> call.
    * @param {Array.<String>} authNames An array of authentication method names.
    */
    applyAuthToRequest(request, authNames) {
        authNames.forEach((authName) => {
            var auth = this.authentications[authName];
            switch (auth.type) {
                case 'basic':
                    if (auth.username || auth.password) {
                        request.auth(auth.username || '', auth.password || '');
                    }

                    break;
                case 'bearer':
                    if (auth.accessToken) {
                        var localVarBearerToken = typeof auth.accessToken === 'function'
                          ? auth.accessToken()
                          : auth.accessToken
                        request.set({'Authorization': 'Bearer ' + localVarBearerToken});
                    }

                    break;
                case 'apiKey':
                    if (auth.apiKey) {
                        var data = {};
                        if (auth.apiKeyPrefix) {
                            data[auth.name] = auth.apiKeyPrefix + ' ' + auth.apiKey;
                        } else {
                            data[auth.name] = auth.apiKey;
                        }

                        if (auth['in'] === 'header') {
                            request.set(data);
                        } else {
                            request.query(data);
                        }
                    }

                    break;
                case 'oauth2':
                    if (auth.accessToken) {
                        request.set({'Authorization': 'Bearer ' + auth.accessToken});
                    }

                    break;
                default:
                    throw new Error('Unknown authentication type: ' + auth.type);
            }
        });
    }

   /**
    * Deserializes an HTTP response body into a value of the specified type.
    * @param {Object} response A SuperAgent response object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} returnType The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns A value of the specified type.
    */
    deserialize(response, returnType) {
        if (response == null || returnType == null || response.status == 204) {
            return null;
        }

        // Rely on SuperAgent for parsing response body.
        // See http://visionmedia.github.io/superagent/#parsing-response-bodies
        var data = response.body;
        if (data == null || (typeof data === 'object' && typeof data.length === 'undefined' && !Object.keys(data).length)) {
            // SuperAgent does not always produce a body; use the unparsed response as a fallback
            data = response.text;
        }

        return ApiClient.convertToType(data, returnType);
    }

   /**
    * Callback function to receive the result of the operation.
    * @callback module:ApiClient~callApiCallback
    * @param {String} error Error message, if any.
    * @param data The data returned by the service call.
    * @param {String} response The complete HTTP response.
    */

   /**
    * Invokes the REST service using the supplied settings and parameters.
    * @param {String} path The base URL to invoke.
    * @param {String} httpMethod The HTTP method to use.
    * @param {Object.<String, String>} pathParams A map of path parameters and their values.
    * @param {Object.<String, Object>} queryParams A map of query parameters and their values.
    * @param {Object.<String, Object>} headerParams A map of header parameters and their values.
    * @param {Object.<String, Object>} formParams A map of form parameters and their values.
    * @param {Object} bodyParam The value to pass as the request body.
    * @param {Array.<String>} authNames An array of authentication type names.
    * @param {Array.<String>} contentTypes An array of request MIME types.
    * @param {Array.<String>} accepts An array of acceptable response MIME types.
    * @param {(String|Array|ObjectFunction)} returnType The required type to return; can be a string for simple types or the
    * constructor for a complex type.
    * @param {String} apiBasePath base path defined in the operation/path level to override the default one
    * @param {module:ApiClient~callApiCallback} callback The callback function.
    * @returns {Object} The SuperAgent request object.
    */
    callApi(path, httpMethod, pathParams,
        queryParams, headerParams, formParams, bodyParam, authNames, contentTypes, accepts,
        returnType, apiBasePath, callback) {

        var url = this.buildUrl(path, pathParams, apiBasePath);
        var request = superagent(httpMethod, url);

        if (this.plugins !== null) {
            for (var index in this.plugins) {
                if (this.plugins.hasOwnProperty(index)) {
                    request.use(this.plugins[index])
                }
            }
        }

        // apply authentications
        this.applyAuthToRequest(request, authNames);

        // set query parameters
        if (httpMethod.toUpperCase() === 'GET' && this.cache === false) {
            queryParams['_'] = new Date().getTime();
        }

        request.query(this.normalizeParams(queryParams));

        // set header parameters
        request.set(this.defaultHeaders).set(this.normalizeParams(headerParams));

        // set requestAgent if it is set by user
        if (this.requestAgent) {
          request.agent(this.requestAgent);
        }

        // set request timeout
        request.timeout(this.timeout);

        var contentType = this.jsonPreferredMime(contentTypes);
        if (contentType) {
            // Issue with superagent and multipart/form-data (https://github.com/visionmedia/superagent/issues/746)
            if(contentType != 'multipart/form-data') {
                request.type(contentType);
            }
        }

        if (contentType === 'application/x-www-form-urlencoded') {
            request.send(querystring.stringify(this.normalizeParams(formParams)));
        } else if (contentType == 'multipart/form-data') {
            var _formParams = this.normalizeParams(formParams);
            for (var key in _formParams) {
                if (_formParams.hasOwnProperty(key)) {
                    let _formParamsValue = _formParams[key];
                    if (this.isFileParam(_formParamsValue)) {
                        // file field
                        request.attach(key, _formParamsValue);
                    } else if (Array.isArray(_formParamsValue) && _formParamsValue.length
                        && this.isFileParam(_formParamsValue[0])) {
                        // multiple files
                        _formParamsValue.forEach(file => request.attach(key, file));
                    } else {
                        request.field(key, _formParamsValue);
                    }
                }
            }
        } else if (bodyParam !== null && bodyParam !== undefined) {
            if (!request.header['Content-Type']) {
                request.type('application/json');
            }
            request.send(bodyParam);
        }

        var accept = this.jsonPreferredMime(accepts);
        if (accept) {
            request.accept(accept);
        }

        if (returnType === 'Blob') {
          request.responseType('blob');
        } else if (returnType === 'String') {
          request.responseType('text');
        }

        // Attach previously saved cookies, if enabled
        if (this.enableCookies){
            if (typeof window === 'undefined') {
                this.agent._attachCookies(request);
            }
            else {
                request.withCredentials();
            }
        }

        request.end((error, response) => {
            if (callback) {
                var data = null;
                if (!error) {
                    try {
                        data = this.deserialize(response, returnType);
                        if (this.enableCookies && typeof window === 'undefined'){
                            this.agent._saveCookies(response);
                        }
                    } catch (err) {
                        error = err;
                    }
                }

                callback(error, data, response);
            }
        });

        return request;
    }

    /**
    * Parses an ISO-8601 string representation or epoch representation of a date value.
    * @param {String} str The date value as a string.
    * @returns {Date} The parsed date object.
    */
    static parseDate(str) {
        if (isNaN(str)) {
            return new Date(str.replace(/(\d)(T)(\d)/i, '$1 $3'));
        }
        return new Date(+str);
    }

    /**
    * Converts a value to the specified type.
    * @param {(String|Object)} data The data to convert, as a string or object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} type The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns An instance of the specified type or null or undefined if data is null or undefined.
    */
    static convertToType(data, type) {
        if (data === null || data === undefined)
            return data

        switch (type) {
            case 'Boolean':
                return Boolean(data);
            case 'Integer':
                return parseInt(data, 10);
            case 'Number':
                return parseFloat(data);
            case 'String':
                return String(data);
            case 'Date':
                return ApiClient.parseDate(String(data));
            case 'Blob':
                return data;
            default:
                if (type === Object) {
                    // generic object, return directly
                    return data;
                } else if (typeof type.constructFromObject === 'function') {
                    // for model type like User and enum class
                    return type.constructFromObject(data);
                } else if (Array.isArray(type)) {
                    // for array type like: ['String']
                    var itemType = type[0];

                    return data.map((item) => {
                        return ApiClient.convertToType(item, itemType);
                    });
                } else if (typeof type === 'object') {
                    // for plain object type like: {'String': 'Integer'}
                    var keyType, valueType;
                    for (var k in type) {
                        if (type.hasOwnProperty(k)) {
                            keyType = k;
                            valueType = type[k];
                            break;
                        }
                    }

                    var result = {};
                    for (var k in data) {
                        if (data.hasOwnProperty(k)) {
                            var key = ApiClient.convertToType(k, keyType);
                            var value = ApiClient.convertToType(data[k], valueType);
                            result[key] = value;
                        }
                    }

                    return result;
                } else {
                    // for unknown type, return the data directly
                    return data;
                }
        }
    }

  /**
    * Gets an array of host settings
    * @returns An array of host settings
    */
    hostSettings() {
        return [
            {
              'url': "https://api.shop-pro.jp",
              'description': "No description provided",
            }
      ];
    }

    getBasePathFromSettings(index, variables={}) {
        var servers = this.hostSettings();

        // check array index out of bound
        if (index < 0 || index >= servers.length) {
            throw new Error("Invalid index " + index + " when selecting the host settings. Must be less than " + servers.length);
        }

        var server = servers[index];
        var url = server['url'];

        // go through variable and assign a value
        for (var variable_name in server['variables']) {
            if (variable_name in variables) {
                let variable = server['variables'][variable_name];
                if ( !('enum_values' in variable) || variable['enum_values'].includes(variables[variable_name]) ) {
                    url = url.replace("{" + variable_name + "}", variables[variable_name]);
                } else {
                    throw new Error("The variable `" + variable_name + "` in the host URL has invalid value " + variables[variable_name] + ". Must be " + server['variables'][variable_name]['enum_values'] + ".");
                }
            } else {
                // use default value
                url = url.replace("{" + variable_name + "}", server['variables'][variable_name]['default_value'])
            }
        }
        return url;
    }

    /**
    * Constructs a new map or array model from REST data.
    * @param data {Object|Array} The REST data.
    * @param obj {Object|Array} The target object or array.
    */
    static constructFromObject(data, obj, itemType) {
        if (Array.isArray(data)) {
            for (var i = 0; i < data.length; i++) {
                if (data.hasOwnProperty(i))
                    obj[i] = ApiClient.convertToType(data[i], itemType);
            }
        } else {
            for (var k in data) {
                if (data.hasOwnProperty(k))
                    obj[k] = ApiClient.convertToType(data[k], itemType);
            }
        }
    };
}

/**
 * Enumeration of collection format separator strategies.
 * @enum {String}
 * @readonly
 */
ApiClient.CollectionFormatEnum = {
    /**
     * Comma-separated values. Value: <code>csv</code>
     * @const
     */
    CSV: ',',

    /**
     * Space-separated values. Value: <code>ssv</code>
     * @const
     */
    SSV: ' ',

    /**
     * Tab-separated values. Value: <code>tsv</code>
     * @const
     */
    TSV: '\t',

    /**
     * Pipe(|)-separated values. Value: <code>pipes</code>
     * @const
     */
    PIPES: '|',

    /**
     * Native array. Value: <code>multi</code>
     * @const
     */
    MULTI: 'multi'
};

/**
* The default API client implementation.
* @type {module:ApiClient}
*/
ApiClient.instance = new ApiClient();
export default ApiClient;
