/**
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIEditSubaccountApi_H
#define OAI_OAIEditSubaccountApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErreur.h"
#include "OAISubaccountRequest.h"
#include "OAISubaccountResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIEditSubaccountApi : public QObject {
    Q_OBJECT

public:
    OAIEditSubaccountApi(const int timeOut = 0);
    ~OAIEditSubaccountApi();

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
    * @param[in]  oai_subaccount_request OAISubaccountRequest [required]
    */
    virtual void subaccountEdit(const OAISubaccountRequest &oai_subaccount_request);


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

    void subaccountEditCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void subaccountEditSignal(OAISubaccountResponse summary);


    void subaccountEditSignalFull(OAIHttpRequestWorker *worker, OAISubaccountResponse summary);

    Q_DECL_DEPRECATED_X("Use subaccountEditSignalError() instead")
    void subaccountEditSignalE(OAISubaccountResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void subaccountEditSignalError(OAISubaccountResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use subaccountEditSignalErrorFull() instead")
    void subaccountEditSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void subaccountEditSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
