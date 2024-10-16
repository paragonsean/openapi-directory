/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBulkAnonymizationData.h
 *
 * 
 */

#ifndef OAIBulkAnonymizationData_H
#define OAIBulkAnonymizationData_H

#include <QJsonObject>

#include "OAIAnonymizationProfile.h"
#include "OAIImageTagValues.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImageTagValues;
class OAIAnonymizationProfile;

class OAIBulkAnonymizationData : public OAIObject {
public:
    OAIBulkAnonymizationData();
    OAIBulkAnonymizationData(QString json);
    ~OAIBulkAnonymizationData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIImageTagValues> getImageTagValuesSet() const;
    void setImageTagValuesSet(const QList<OAIImageTagValues> &image_tag_values_set);
    bool is_image_tag_values_set_Set() const;
    bool is_image_tag_values_set_Valid() const;

    OAIAnonymizationProfile getProfile() const;
    void setProfile(const OAIAnonymizationProfile &profile);
    bool is_profile_Set() const;
    bool is_profile_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIImageTagValues> m_image_tag_values_set;
    bool m_image_tag_values_set_isSet;
    bool m_image_tag_values_set_isValid;

    OAIAnonymizationProfile m_profile;
    bool m_profile_isSet;
    bool m_profile_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBulkAnonymizationData)

#endif // OAIBulkAnonymizationData_H
