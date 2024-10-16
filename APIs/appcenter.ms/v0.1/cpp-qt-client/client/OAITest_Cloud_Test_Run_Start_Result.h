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
 * OAITest_Cloud_Test_Run_Start_Result.h
 *
 * Result of starting a test run
 */

#ifndef OAITest_Cloud_Test_Run_Start_Result_H
#define OAITest_Cloud_Test_Run_Start_Result_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_Cloud_Test_Run_Start_Result : public OAIObject {
public:
    OAITest_Cloud_Test_Run_Start_Result();
    OAITest_Cloud_Test_Run_Start_Result(QString json);
    ~OAITest_Cloud_Test_Run_Start_Result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAcceptedDevices() const;
    void setAcceptedDevices(const QList<QString> &accepted_devices);
    bool is_accepted_devices_Set() const;
    bool is_accepted_devices_Valid() const;

    QList<QString> getRejectedDevices() const;
    void setRejectedDevices(const QList<QString> &rejected_devices);
    bool is_rejected_devices_Set() const;
    bool is_rejected_devices_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_accepted_devices;
    bool m_accepted_devices_isSet;
    bool m_accepted_devices_isValid;

    QList<QString> m_rejected_devices;
    bool m_rejected_devices_isSet;
    bool m_rejected_devices_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_Cloud_Test_Run_Start_Result)

#endif // OAITest_Cloud_Test_Run_Start_Result_H
