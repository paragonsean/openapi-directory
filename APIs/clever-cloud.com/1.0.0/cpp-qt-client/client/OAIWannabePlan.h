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
 * OAIWannabePlan.h
 *
 * 
 */

#ifndef OAIWannabePlan_H
#define OAIWannabePlan_H

#include <QJsonObject>

#include "OAIWannabePlanFeature.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWannabePlanFeature;

class OAIWannabePlan : public OAIObject {
public:
    OAIWannabePlan();
    OAIWannabePlan(QString json);
    ~OAIWannabePlan() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIWannabePlanFeature> getFeatures() const;
    void setFeatures(const QList<OAIWannabePlanFeature> &features);
    bool is_features_Set() const;
    bool is_features_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint64 getPrice() const;
    void setPrice(const qint64 &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getSlug() const;
    void setSlug(const QString &slug);
    bool is_slug_Set() const;
    bool is_slug_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIWannabePlanFeature> m_features;
    bool m_features_isSet;
    bool m_features_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint64 m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_slug;
    bool m_slug_isSet;
    bool m_slug_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWannabePlan)

#endif // OAIWannabePlan_H
