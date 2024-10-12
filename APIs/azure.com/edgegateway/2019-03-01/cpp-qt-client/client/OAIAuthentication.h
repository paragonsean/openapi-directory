/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAuthentication.h
 *
 * Authentication mechanism for IoT devices.
 */

#ifndef OAIAuthentication_H
#define OAIAuthentication_H

#include <QJsonObject>

#include "OAISymmetricKey.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISymmetricKey;

class OAIAuthentication : public OAIObject {
public:
    OAIAuthentication();
    OAIAuthentication(QString json);
    ~OAIAuthentication() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISymmetricKey getSymmetricKey() const;
    void setSymmetricKey(const OAISymmetricKey &symmetric_key);
    bool is_symmetric_key_Set() const;
    bool is_symmetric_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISymmetricKey m_symmetric_key;
    bool m_symmetric_key_isSet;
    bool m_symmetric_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAuthentication)

#endif // OAIAuthentication_H
