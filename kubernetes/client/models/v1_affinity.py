# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Affinity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, node_affinity=None, pod_affinity=None, pod_anti_affinity=None):
        """
        V1Affinity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'node_affinity': 'V1NodeAffinity',
            'pod_affinity': 'V1PodAffinity',
            'pod_anti_affinity': 'V1PodAntiAffinity'
        }

        self.attribute_map = {
            'node_affinity': 'nodeAffinity',
            'pod_affinity': 'podAffinity',
            'pod_anti_affinity': 'podAntiAffinity'
        }

        self._node_affinity = node_affinity
        self._pod_affinity = pod_affinity
        self._pod_anti_affinity = pod_anti_affinity

    @property
    def node_affinity(self):
        """
        Gets the node_affinity of this V1Affinity.
        Describes node affinity scheduling rules for the pod.

        :return: The node_affinity of this V1Affinity.
        :rtype: V1NodeAffinity
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """
        Sets the node_affinity of this V1Affinity.
        Describes node affinity scheduling rules for the pod.

        :param node_affinity: The node_affinity of this V1Affinity.
        :type: V1NodeAffinity
        """

        self._node_affinity = node_affinity

    @property
    def pod_affinity(self):
        """
        Gets the pod_affinity of this V1Affinity.
        Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

        :return: The pod_affinity of this V1Affinity.
        :rtype: V1PodAffinity
        """
        return self._pod_affinity

    @pod_affinity.setter
    def pod_affinity(self, pod_affinity):
        """
        Sets the pod_affinity of this V1Affinity.
        Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

        :param pod_affinity: The pod_affinity of this V1Affinity.
        :type: V1PodAffinity
        """

        self._pod_affinity = pod_affinity

    @property
    def pod_anti_affinity(self):
        """
        Gets the pod_anti_affinity of this V1Affinity.
        Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :return: The pod_anti_affinity of this V1Affinity.
        :rtype: V1PodAntiAffinity
        """
        return self._pod_anti_affinity

    @pod_anti_affinity.setter
    def pod_anti_affinity(self, pod_anti_affinity):
        """
        Sets the pod_anti_affinity of this V1Affinity.
        Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :param pod_anti_affinity: The pod_anti_affinity of this V1Affinity.
        :type: V1PodAntiAffinity
        """

        self._pod_anti_affinity = pod_anti_affinity

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Affinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other