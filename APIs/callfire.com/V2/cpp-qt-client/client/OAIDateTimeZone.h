/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDateTimeZone.h
 *
 * ~
 */

#ifndef OAIDateTimeZone_H
#define OAIDateTimeZone_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDateTimeZone : public OAIObject {
public:
    OAIDateTimeZone();
    OAIDateTimeZone(QString json);
    ~OAIDateTimeZone() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isFixed() const;
    void setFixed(const bool &fixed);
    bool is_fixed_Set() const;
    bool is_fixed_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_fixed;
    bool m_fixed_isSet;
    bool m_fixed_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDateTimeZone)

#endif // OAIDateTimeZone_H
