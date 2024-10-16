/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIVoiceSettingsResponseModel.h
 *
 * 
 */

#ifndef OAIVoiceSettingsResponseModel_H
#define OAIVoiceSettingsResponseModel_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVoiceSettingsResponseModel : public OAIObject {
public:
    OAIVoiceSettingsResponseModel();
    OAIVoiceSettingsResponseModel(QString json);
    ~OAIVoiceSettingsResponseModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getSimilarityBoost() const;
    void setSimilarityBoost(const double &similarity_boost);
    bool is_similarity_boost_Set() const;
    bool is_similarity_boost_Valid() const;

    double getStability() const;
    void setStability(const double &stability);
    bool is_stability_Set() const;
    bool is_stability_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_similarity_boost;
    bool m_similarity_boost_isSet;
    bool m_similarity_boost_isValid;

    double m_stability;
    bool m_stability_isSet;
    bool m_stability_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVoiceSettingsResponseModel)

#endif // OAIVoiceSettingsResponseModel_H
