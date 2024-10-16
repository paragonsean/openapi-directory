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
 * OAIArchIdentifier.h
 *
 * An object containing a UUID for an architecture for an iOS app.
 */

#ifndef OAIArchIdentifier_H
#define OAIArchIdentifier_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArchIdentifier : public OAIObject {
public:
    OAIArchIdentifier();
    OAIArchIdentifier(QString json);
    ~OAIArchIdentifier() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArchitecture() const;
    void setArchitecture(const QString &architecture);
    bool is_architecture_Set() const;
    bool is_architecture_Valid() const;

    QString getUuid() const;
    void setUuid(const QString &uuid);
    bool is_uuid_Set() const;
    bool is_uuid_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_architecture;
    bool m_architecture_isSet;
    bool m_architecture_isValid;

    QString m_uuid;
    bool m_uuid_isSet;
    bool m_uuid_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArchIdentifier)

#endif // OAIArchIdentifier_H
