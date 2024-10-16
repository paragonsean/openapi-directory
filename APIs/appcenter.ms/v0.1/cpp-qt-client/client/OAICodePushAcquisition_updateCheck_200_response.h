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
 * OAICodePushAcquisition_updateCheck_200_response.h
 *
 * 
 */

#ifndef OAICodePushAcquisition_updateCheck_200_response_H
#define OAICodePushAcquisition_updateCheck_200_response_H

#include <QJsonObject>

#include "OAICodePushAcquisition_updateCheck_200_response_update_info.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICodePushAcquisition_updateCheck_200_response_update_info;

class OAICodePushAcquisition_updateCheck_200_response : public OAIObject {
public:
    OAICodePushAcquisition_updateCheck_200_response();
    OAICodePushAcquisition_updateCheck_200_response(QString json);
    ~OAICodePushAcquisition_updateCheck_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICodePushAcquisition_updateCheck_200_response_update_info getUpdateInfo() const;
    void setUpdateInfo(const OAICodePushAcquisition_updateCheck_200_response_update_info &update_info);
    bool is_update_info_Set() const;
    bool is_update_info_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICodePushAcquisition_updateCheck_200_response_update_info m_update_info;
    bool m_update_info_isSet;
    bool m_update_info_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICodePushAcquisition_updateCheck_200_response)

#endif // OAICodePushAcquisition_updateCheck_200_response_H
