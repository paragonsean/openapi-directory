/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICloudError.h
 *
 * An error response from the service.
 */

#ifndef OAICloudError_H
#define OAICloudError_H

#include <QJsonObject>

#include "OAICloudErrorBody.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICloudErrorBody;

class OAICloudError : public OAIObject {
public:
    OAICloudError();
    OAICloudError(QString json);
    ~OAICloudError() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICloudErrorBody getError() const;
    void setError(const OAICloudErrorBody &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICloudErrorBody m_error;
    bool m_error_isSet;
    bool m_error_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICloudError)

#endif // OAICloudError_H
