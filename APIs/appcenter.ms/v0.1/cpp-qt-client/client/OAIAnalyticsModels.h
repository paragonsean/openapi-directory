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
 * OAIAnalyticsModels.h
 *
 * 
 */

#ifndef OAIAnalyticsModels_H
#define OAIAnalyticsModels_H

#include <QJsonObject>

#include "OAIAnalytics_ModelCounts_200_response_models_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAnalytics_ModelCounts_200_response_models_inner;

class OAIAnalyticsModels : public OAIObject {
public:
    OAIAnalyticsModels();
    OAIAnalyticsModels(QString json);
    ~OAIAnalyticsModels() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAnalytics_ModelCounts_200_response_models_inner> getModels() const;
    void setModels(const QList<OAIAnalytics_ModelCounts_200_response_models_inner> &models);
    bool is_models_Set() const;
    bool is_models_Valid() const;

    qint64 getTotal() const;
    void setTotal(const qint64 &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAnalytics_ModelCounts_200_response_models_inner> m_models;
    bool m_models_isSet;
    bool m_models_isValid;

    qint64 m_total;
    bool m_total_isSet;
    bool m_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnalyticsModels)

#endif // OAIAnalyticsModels_H
