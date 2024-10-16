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
 * OAIAnonymizationProfile.h
 *
 * 
 */

#ifndef OAIAnonymizationProfile_H
#define OAIAnonymizationProfile_H

#include <QJsonObject>

#include "OAIConfidentialityOption.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfidentialityOption;

class OAIAnonymizationProfile : public OAIObject {
public:
    OAIAnonymizationProfile();
    OAIAnonymizationProfile(QString json);
    ~OAIAnonymizationProfile() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIConfidentialityOption> getOptions() const;
    void setOptions(const QList<OAIConfidentialityOption> &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIConfidentialityOption> m_options;
    bool m_options_isSet;
    bool m_options_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnonymizationProfile)

#endif // OAIAnonymizationProfile_H
