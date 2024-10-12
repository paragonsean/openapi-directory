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
 * OAISessionResponse.h
 *
 * 
 */

#ifndef OAISessionResponse_H
#define OAISessionResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISessionResponse : public OAIObject {
public:
    OAISessionResponse();
    OAISessionResponse(QString json);
    ~OAISessionResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessToken() const;
    void setAccessToken(const QString &access_token);
    bool is_access_token_Set() const;
    bool is_access_token_Valid() const;

    qint32 getExpiresIn() const;
    void setExpiresIn(const qint32 &expires_in);
    bool is_expires_in_Set() const;
    bool is_expires_in_Valid() const;

    qint32 getRefreshExpiresIn() const;
    void setRefreshExpiresIn(const qint32 &refresh_expires_in);
    bool is_refresh_expires_in_Set() const;
    bool is_refresh_expires_in_Valid() const;

    QString getRefreshToken() const;
    void setRefreshToken(const QString &refresh_token);
    bool is_refresh_token_Set() const;
    bool is_refresh_token_Valid() const;

    QString getTokenType() const;
    void setTokenType(const QString &token_type);
    bool is_token_type_Set() const;
    bool is_token_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_token;
    bool m_access_token_isSet;
    bool m_access_token_isValid;

    qint32 m_expires_in;
    bool m_expires_in_isSet;
    bool m_expires_in_isValid;

    qint32 m_refresh_expires_in;
    bool m_refresh_expires_in_isSet;
    bool m_refresh_expires_in_isValid;

    QString m_refresh_token;
    bool m_refresh_token_isSet;
    bool m_refresh_token_isValid;

    QString m_token_type;
    bool m_token_type_isSet;
    bool m_token_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISessionResponse)

#endif // OAISessionResponse_H
