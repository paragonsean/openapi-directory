/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFeature.h
 *
 * Feature
 */

#ifndef OAIFeature_H
#define OAIFeature_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFeature : public OAIObject {
public:
    OAIFeature();
    OAIFeature(QString json);
    ~OAIFeature() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getFeatureId() const;
    void setFeatureId(const qint32 &feature_id);
    bool is_feature_id_Set() const;
    bool is_feature_id_Valid() const;

    QString getFeatureName() const;
    void setFeatureName(const QString &feature_name);
    bool is_feature_name_Set() const;
    bool is_feature_name_Valid() const;

    bool isIsAvailable() const;
    void setIsAvailable(const bool &is_available);
    bool is_is_available_Set() const;
    bool is_is_available_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_feature_id;
    bool m_feature_id_isSet;
    bool m_feature_id_isValid;

    QString m_feature_name;
    bool m_feature_name_isSet;
    bool m_feature_name_isValid;

    bool m_is_available;
    bool m_is_available_isSet;
    bool m_is_available_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFeature)

#endif // OAIFeature_H
