/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRegisterPayload.h
 *
 * Represents payload for Register action.
 */

#ifndef OAIRegisterPayload_H
#define OAIRegisterPayload_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRegisterPayload : public OAIObject {
public:
    OAIRegisterPayload();
    OAIRegisterPayload(QString json);
    ~OAIRegisterPayload() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRegistrationCode() const;
    void setRegistrationCode(const QString &registration_code);
    bool is_registration_code_Set() const;
    bool is_registration_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_registration_code;
    bool m_registration_code_isSet;
    bool m_registration_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRegisterPayload)

#endif // OAIRegisterPayload_H
