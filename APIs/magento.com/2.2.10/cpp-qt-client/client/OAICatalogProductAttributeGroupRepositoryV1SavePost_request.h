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
 * OAICatalogProductAttributeGroupRepositoryV1SavePost_request.h
 *
 * 
 */

#ifndef OAICatalogProductAttributeGroupRepositoryV1SavePost_request_H
#define OAICatalogProductAttributeGroupRepositoryV1SavePost_request_H

#include <QJsonObject>

#include "OAIEav_data_attribute_group_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEav_data_attribute_group_interface;

class OAICatalogProductAttributeGroupRepositoryV1SavePost_request : public OAIObject {
public:
    OAICatalogProductAttributeGroupRepositoryV1SavePost_request();
    OAICatalogProductAttributeGroupRepositoryV1SavePost_request(QString json);
    ~OAICatalogProductAttributeGroupRepositoryV1SavePost_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIEav_data_attribute_group_interface getGroup() const;
    void setGroup(const OAIEav_data_attribute_group_interface &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIEav_data_attribute_group_interface m_group;
    bool m_group_isSet;
    bool m_group_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalogProductAttributeGroupRepositoryV1SavePost_request)

#endif // OAICatalogProductAttributeGroupRepositoryV1SavePost_request_H
