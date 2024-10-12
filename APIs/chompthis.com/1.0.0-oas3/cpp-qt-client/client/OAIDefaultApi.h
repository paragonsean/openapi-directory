/**
 * Chomp Food Database API Documentation
 * ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &raquo;](https://chompthis.com/api/)     * [Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php) 
 *
 * The version of the OpenAPI document: 1.0.0-oas3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBrandedFoodObject.h"
#include "OAIIngredientObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  code QString [required]
    */
    virtual void foodBrandedBarcodePhpGet(const QString &code);

    /**
    * @param[in]  name QString [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  page qint32 [optional]
    */
    virtual void foodBrandedNamePhpGet(const QString &name, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  allergen QString [optional]
    * @param[in]  brand QString [optional]
    * @param[in]  category QString [optional]
    * @param[in]  country QString [optional]
    * @param[in]  diet QString [optional]
    * @param[in]  ingredient QString [optional]
    * @param[in]  keyword QString [optional]
    * @param[in]  mineral QString [optional]
    * @param[in]  nutrient QString [optional]
    * @param[in]  palm_oil QString [optional]
    * @param[in]  trace QString [optional]
    * @param[in]  vitamin QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  page qint32 [optional]
    */
    virtual void foodBrandedSearchPhpGet(const ::OpenAPI::OptionalParam<QString> &allergen = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &brand = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &category = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &country = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &diet = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ingredient = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &keyword = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &mineral = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &nutrient = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &palm_oil = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trace = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &vitamin = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  find QString [required]
    * @param[in]  limit qint32 [optional]
    */
    virtual void foodIngredientSearchPhpGet(const QString &find, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void foodBrandedBarcodePhpGetCallback(OAIHttpRequestWorker *worker);
    void foodBrandedNamePhpGetCallback(OAIHttpRequestWorker *worker);
    void foodBrandedSearchPhpGetCallback(OAIHttpRequestWorker *worker);
    void foodIngredientSearchPhpGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void foodBrandedBarcodePhpGetSignal(OAIBrandedFoodObject summary);
    void foodBrandedNamePhpGetSignal(OAIBrandedFoodObject summary);
    void foodBrandedSearchPhpGetSignal(OAIBrandedFoodObject summary);
    void foodIngredientSearchPhpGetSignal(OAIIngredientObject summary);


    void foodBrandedBarcodePhpGetSignalFull(OAIHttpRequestWorker *worker, OAIBrandedFoodObject summary);
    void foodBrandedNamePhpGetSignalFull(OAIHttpRequestWorker *worker, OAIBrandedFoodObject summary);
    void foodBrandedSearchPhpGetSignalFull(OAIHttpRequestWorker *worker, OAIBrandedFoodObject summary);
    void foodIngredientSearchPhpGetSignalFull(OAIHttpRequestWorker *worker, OAIIngredientObject summary);

    Q_DECL_DEPRECATED_X("Use foodBrandedBarcodePhpGetSignalError() instead")
    void foodBrandedBarcodePhpGetSignalE(OAIBrandedFoodObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void foodBrandedBarcodePhpGetSignalError(OAIBrandedFoodObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use foodBrandedNamePhpGetSignalError() instead")
    void foodBrandedNamePhpGetSignalE(OAIBrandedFoodObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void foodBrandedNamePhpGetSignalError(OAIBrandedFoodObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use foodBrandedSearchPhpGetSignalError() instead")
    void foodBrandedSearchPhpGetSignalE(OAIBrandedFoodObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void foodBrandedSearchPhpGetSignalError(OAIBrandedFoodObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use foodIngredientSearchPhpGetSignalError() instead")
    void foodIngredientSearchPhpGetSignalE(OAIIngredientObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void foodIngredientSearchPhpGetSignalError(OAIIngredientObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use foodBrandedBarcodePhpGetSignalErrorFull() instead")
    void foodBrandedBarcodePhpGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void foodBrandedBarcodePhpGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use foodBrandedNamePhpGetSignalErrorFull() instead")
    void foodBrandedNamePhpGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void foodBrandedNamePhpGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use foodBrandedSearchPhpGetSignalErrorFull() instead")
    void foodBrandedSearchPhpGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void foodBrandedSearchPhpGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use foodIngredientSearchPhpGetSignalErrorFull() instead")
    void foodIngredientSearchPhpGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void foodIngredientSearchPhpGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
