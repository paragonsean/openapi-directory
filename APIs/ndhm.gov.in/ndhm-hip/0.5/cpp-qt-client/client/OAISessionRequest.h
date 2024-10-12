/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISessionRequest.h
 *
 * 
 */

#ifndef OAISessionRequest_H
#define OAISessionRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISessionRequest : public OAIObject {
public:
    OAISessionRequest();
    OAISessionRequest(QString json);
    ~OAISessionRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QString getClientSecret() const;
    void setClientSecret(const QString &client_secret);
    bool is_client_secret_Set() const;
    bool is_client_secret_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QString m_client_secret;
    bool m_client_secret_isSet;
    bool m_client_secret_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISessionRequest)

#endif // OAISessionRequest_H
