/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConso.h
 *
 * 
 */

#ifndef OAIConso_H
#define OAIConso_H

#include <QJsonObject>

#include "OAIConso_conso.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConso_conso;

class OAIConso : public OAIObject {
public:
    OAIConso();
    OAIConso(QString json);
    ~OAIConso() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAppId() const;
    void setAppId(const QString &app_id);
    bool is_app_id_Set() const;
    bool is_app_id_Valid() const;

    OAIConso_conso getConso() const;
    void setConso(const OAIConso_conso &conso);
    bool is_conso_Set() const;
    bool is_conso_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_app_id;
    bool m_app_id_isSet;
    bool m_app_id_isValid;

    OAIConso_conso m_conso;
    bool m_conso_isSet;
    bool m_conso_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConso)

#endif // OAIConso_H
