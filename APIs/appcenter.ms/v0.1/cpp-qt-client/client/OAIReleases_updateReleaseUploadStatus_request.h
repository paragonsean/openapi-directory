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
 * OAIReleases_updateReleaseUploadStatus_request.h
 *
 * 
 */

#ifndef OAIReleases_updateReleaseUploadStatus_request_H
#define OAIReleases_updateReleaseUploadStatus_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIReleases_updateReleaseUploadStatus_request : public OAIObject {
public:
    OAIReleases_updateReleaseUploadStatus_request();
    OAIReleases_updateReleaseUploadStatus_request(QString json);
    ~OAIReleases_updateReleaseUploadStatus_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUploadStatus() const;
    void setUploadStatus(const QString &upload_status);
    bool is_upload_status_Set() const;
    bool is_upload_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_upload_status;
    bool m_upload_status_isSet;
    bool m_upload_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReleases_updateReleaseUploadStatus_request)

#endif // OAIReleases_updateReleaseUploadStatus_request_H
