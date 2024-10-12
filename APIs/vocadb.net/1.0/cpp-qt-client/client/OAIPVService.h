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
 * OAIPVService.h
 *
 * 
 */

#ifndef OAIPVService_H
#define OAIPVService_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPVService : public OAIEnum {
public:
    OAIPVService();
    OAIPVService(QString json);
    ~OAIPVService() override;

    QString asJson() const override;
    QJsonValue asJsonValue() const override;
    void fromJsonValue(QJsonValue json) override;
    void fromJson(QString jsonString) override;

    enum class eOAIPVService {
        INVALID_VALUE_OPENAPI_GENERATED = 0,
        NICONICODOUGA, 
        YOUTUBE, 
        SOUNDCLOUD, 
        VIMEO, 
        PIAPRO, 
        BILIBILI, 
        FILE, 
        LOCALFILE, 
        CREOFUGA, 
        BANDCAMP
    };
    OAIPVService::eOAIPVService getValue() const;
    void setValue(const OAIPVService::eOAIPVService& value);
    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    eOAIPVService m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPVService)

#endif // OAIPVService_H
