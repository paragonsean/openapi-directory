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
 * OAICompanyCompanyHierarchyV1MoveNodePut_request.h
 *
 * 
 */

#ifndef OAICompanyCompanyHierarchyV1MoveNodePut_request_H
#define OAICompanyCompanyHierarchyV1MoveNodePut_request_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICompanyCompanyHierarchyV1MoveNodePut_request : public OAIObject {
public:
    OAICompanyCompanyHierarchyV1MoveNodePut_request();
    OAICompanyCompanyHierarchyV1MoveNodePut_request(QString json);
    ~OAICompanyCompanyHierarchyV1MoveNodePut_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getNewParentId() const;
    void setNewParentId(const qint32 &new_parent_id);
    bool is_new_parent_id_Set() const;
    bool is_new_parent_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_new_parent_id;
    bool m_new_parent_id_isSet;
    bool m_new_parent_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICompanyCompanyHierarchyV1MoveNodePut_request)

#endif // OAICompanyCompanyHierarchyV1MoveNodePut_request_H
