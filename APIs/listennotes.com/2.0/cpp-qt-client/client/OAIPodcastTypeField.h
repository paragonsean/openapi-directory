/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPodcastTypeField.h
 *
 * The type of this podcast - episodic or serial.
 */

#ifndef OAIPodcastTypeField_H
#define OAIPodcastTypeField_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPodcastTypeField : public OAIEnum {
public:
    OAIPodcastTypeField();
    OAIPodcastTypeField(QString json);
    ~OAIPodcastTypeField() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIPodcastTypeField {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        EPISODIC, 
        SERIAL
    };
    OAIPodcastTypeField::eOAIPodcastTypeField getValue() const;
    void setValue(const OAIPodcastTypeField::eOAIPodcastTypeField& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIPodcastTypeField m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPodcastTypeField)

#endif // OAIPodcastTypeField_H
