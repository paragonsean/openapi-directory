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
 * OAIEntryType.h
 *
 * 
 */

#ifndef OAIEntryType_H
#define OAIEntryType_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEntryType : public OAIEnum {
public:
    OAIEntryType();
    OAIEntryType(QString json);
    ~OAIEntryType() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIEntryType {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        UNDEFINED, 
        ALBUM, 
        ARTIST, 
        DISCUSSIONTOPIC, 
        PV, 
        RELEASEEVENT, 
        RELEASEEVENTSERIES, 
        SONG, 
        SONGLIST, 
        TAG, 
        USER, 
        VENUE
    };
    OAIEntryType::eOAIEntryType getValue() const;
    void setValue(const OAIEntryType::eOAIEntryType& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIEntryType m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEntryType)

#endif // OAIEntryType_H
