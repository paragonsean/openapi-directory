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
 * OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full.h
 *
 * 
 */

#ifndef OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full_H
#define OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full : public OAIObject {
public:
    OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full();
    OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full(QString json);
    ~OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFrameUrl() const;
    void setFrameUrl(const QString &frame_url);
    bool is_frame_url_Set() const;
    bool is_frame_url_Valid() const;

    double getHeight() const;
    void setHeight(const double &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    QList<double> getScreen() const;
    void setScreen(const QList<double> &screen);
    bool is_screen_Set() const;
    bool is_screen_Valid() const;

    double getWidth() const;
    void setWidth(const double &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_frame_url;
    bool m_frame_url_isSet;
    bool m_frame_url_isValid;

    double m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QList<double> m_screen;
    bool m_screen_isSet;
    bool m_screen_isValid;

    double m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full)

#endif // OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full_H
