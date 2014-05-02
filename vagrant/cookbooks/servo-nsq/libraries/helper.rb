module ServoNSQ
  # Namespacing the Helpers module.
  module Helpers
    # Return the IPv4 (default) address of the given interface.
    #
    # @param [String] interface The interface to query.
    # @param [String] family The protocol family to use.
    # @return [String] The address.
    def address_for(interface, family = 'inet')
      interface_node = node['network']['interfaces'][interface]['addresses']
      interface_node.select do |address, data|
        return address if data['family'] == family
      end
    end
  end
end
