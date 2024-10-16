/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApiTokenDeleteResponse.h
 *
 * 
 */

#ifndef OAIApiTokenDeleteResponse_H
#define OAIApiTokenDeleteResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApiTokenDeleteResponse : public OAIObject {
public:
    OAIApiTokenDeleteResponse();
    OAIApiTokenDeleteResponse(QString json);
    ~OAIApiTokenDeleteResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getTokenHash() const;
    void setTokenHash(const QString &token_hash);
    bool is_token_hash_Set() const;
    bool is_token_hash_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_token_hash;
    bool m_token_hash_isSet;
    bool m_token_hash_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApiTokenDeleteResponse)

#endif // OAIApiTokenDeleteResponse_H
