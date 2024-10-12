/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICatalogAttributeSetManagementV1CreatePost_request.h
 *
 * 
 */

#ifndef OAICatalogAttributeSetManagementV1CreatePost_request_H
#define OAICatalogAttributeSetManagementV1CreatePost_request_H

#include <QJsonObject>

#include "OAIEav_data_attribute_set_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEav_data_attribute_set_interface;

class OAICatalogAttributeSetManagementV1CreatePost_request : public OAIObject {
public:
    OAICatalogAttributeSetManagementV1CreatePost_request();
    OAICatalogAttributeSetManagementV1CreatePost_request(QString json);
    ~OAICatalogAttributeSetManagementV1CreatePost_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIEav_data_attribute_set_interface getAttributeSet() const;
    void setAttributeSet(const OAIEav_data_attribute_set_interface &attribute_set);
    bool is_attribute_set_Set() const;
    bool is_attribute_set_Valid() const;

    qint32 getSkeletonId() const;
    void setSkeletonId(const qint32 &skeleton_id);
    bool is_skeleton_id_Set() const;
    bool is_skeleton_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIEav_data_attribute_set_interface m_attribute_set;
    bool m_attribute_set_isSet;
    bool m_attribute_set_isValid;

    qint32 m_skeleton_id;
    bool m_skeleton_id_isSet;
    bool m_skeleton_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalogAttributeSetManagementV1CreatePost_request)

#endif // OAICatalogAttributeSetManagementV1CreatePost_request_H
