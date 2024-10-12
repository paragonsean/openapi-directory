/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArtistRoles.h
 *
 * 
 */

#ifndef OAIArtistRoles_H
#define OAIArtistRoles_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArtistRoles : public OAIEnum {
public:
    OAIArtistRoles();
    OAIArtistRoles(QString json);
    ~OAIArtistRoles() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIArtistRoles {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        DEFAULT, 
        ANIMATOR, 
        ARRANGER, 
        COMPOSER, 
        DISTRIBUTOR, 
        ILLUSTRATOR, 
        INSTRUMENTALIST, 
        LYRICIST, 
        MASTERING, 
        PUBLISHER, 
        VOCALIST, 
        VOICEMANIPULATOR, 
        OTHER, 
        MIXER, 
        CHORUS, 
        ENCODER, 
        VOCALDATAPROVIDER
    };
    OAIArtistRoles::eOAIArtistRoles getValue() const;
    void setValue(const OAIArtistRoles::eOAIArtistRoles& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIArtistRoles m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArtistRoles)

#endif // OAIArtistRoles_H
