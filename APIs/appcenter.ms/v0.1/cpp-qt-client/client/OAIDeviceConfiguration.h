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
 * OAIDeviceConfiguration.h
 *
 * 
 */

#ifndef OAIDeviceConfiguration_H
#define OAIDeviceConfiguration_H

#include <QJsonObject>

#include "OAITest_getDeviceConfigurations_200_response_inner_image.h"
#include "OAITest_getDeviceConfigurations_200_response_inner_model.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITest_getDeviceConfigurations_200_response_inner_image;
class OAITest_getDeviceConfigurations_200_response_inner_model;

class OAIDeviceConfiguration : public OAIObject {
public:
    OAIDeviceConfiguration();
    OAIDeviceConfiguration(QString json);
    ~OAIDeviceConfiguration() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAITest_getDeviceConfigurations_200_response_inner_image getImage() const;
    void setImage(const OAITest_getDeviceConfigurations_200_response_inner_image &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    double getMarketShare() const;
    void setMarketShare(const double &market_share);
    bool is_market_share_Set() const;
    bool is_market_share_Valid() const;

    OAITest_getDeviceConfigurations_200_response_inner_model getModel() const;
    void setModel(const OAITest_getDeviceConfigurations_200_response_inner_model &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOs() const;
    void setOs(const QString &os);
    bool is_os_Set() const;
    bool is_os_Valid() const;

    QString getOsName() const;
    void setOsName(const QString &os_name);
    bool is_os_name_Set() const;
    bool is_os_name_Valid() const;

    double getTier() const;
    void setTier(const double &tier);
    bool is_tier_Set() const;
    bool is_tier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAITest_getDeviceConfigurations_200_response_inner_image m_image;
    bool m_image_isSet;
    bool m_image_isValid;

    double m_market_share;
    bool m_market_share_isSet;
    bool m_market_share_isValid;

    OAITest_getDeviceConfigurations_200_response_inner_model m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_os;
    bool m_os_isSet;
    bool m_os_isValid;

    QString m_os_name;
    bool m_os_name_isSet;
    bool m_os_name_isValid;

    double m_tier;
    bool m_tier_isSet;
    bool m_tier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeviceConfiguration)

#endif // OAIDeviceConfiguration_H
