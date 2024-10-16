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
 * OAITest_getTestReport_200_response_snapshot_fatal_errors_inner.h
 *
 * 
 */

#ifndef OAITest_getTestReport_200_response_snapshot_fatal_errors_inner_H
#define OAITest_getTestReport_200_response_snapshot_fatal_errors_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_getTestReport_200_response_snapshot_fatal_errors_inner : public OAIObject {
public:
    OAITest_getTestReport_200_response_snapshot_fatal_errors_inner();
    OAITest_getTestReport_200_response_snapshot_fatal_errors_inner(QString json);
    ~OAITest_getTestReport_200_response_snapshot_fatal_errors_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDeviceSnapshotId() const;
    void setDeviceSnapshotId(const QString &device_snapshot_id);
    bool is_device_snapshot_id_Set() const;
    bool is_device_snapshot_id_Valid() const;

    QString getErrorMessage() const;
    void setErrorMessage(const QString &error_message);
    bool is_error_message_Set() const;
    bool is_error_message_Valid() const;

    QString getErrorTitle() const;
    void setErrorTitle(const QString &error_title);
    bool is_error_title_Set() const;
    bool is_error_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_device_snapshot_id;
    bool m_device_snapshot_id_isSet;
    bool m_device_snapshot_id_isValid;

    QString m_error_message;
    bool m_error_message_isSet;
    bool m_error_message_isValid;

    QString m_error_title;
    bool m_error_title_isSet;
    bool m_error_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_getTestReport_200_response_snapshot_fatal_errors_inner)

#endif // OAITest_getTestReport_200_response_snapshot_fatal_errors_inner_H
