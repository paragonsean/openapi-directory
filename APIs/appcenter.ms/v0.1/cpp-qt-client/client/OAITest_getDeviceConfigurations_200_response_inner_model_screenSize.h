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
 * OAITest_getDeviceConfigurations_200_response_inner_model_screenSize.h
 *
 * Physical device screen dimensions
 */

#ifndef OAITest_getDeviceConfigurations_200_response_inner_model_screenSize_H
#define OAITest_getDeviceConfigurations_200_response_inner_model_screenSize_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_getDeviceConfigurations_200_response_inner_model_screenSize : public OAIObject {
public:
    OAITest_getDeviceConfigurations_200_response_inner_model_screenSize();
    OAITest_getDeviceConfigurations_200_response_inner_model_screenSize(QString json);
    ~OAITest_getDeviceConfigurations_200_response_inner_model_screenSize() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCm() const;
    void setCm(const QString &cm);
    bool is_cm_Set() const;
    bool is_cm_Valid() const;

    QString getIn() const;
    void setIn(const QString &in);
    bool is_in_Set() const;
    bool is_in_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_cm;
    bool m_cm_isSet;
    bool m_cm_isValid;

    QString m_in;
    bool m_in_isSet;
    bool m_in_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_getDeviceConfigurations_200_response_inner_model_screenSize)

#endif // OAITest_getDeviceConfigurations_200_response_inner_model_screenSize_H
