INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT INTO `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`) 
VALUES ('FCB', 'FC Barcelona Jersey', 50.00, 100, 'static/images/fcb_jersey.jpeg', 'Sport');

INSERT INTO `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`) 
VALUES ('ACM', 'AC Milan Jersey', 50.00, 100, 'static/images/acm_jersey.jpeg', 'Sport');

INSERT INTO `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('RMA', 'Real Madrid Jersey', 50.00, 100, 'static/images/rma_jersey.jpeg', 'Sport');

INSERT INTO `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`) 
VALUES ('ARS', 'Arsenal Jersey', 50.00, 100, 'static/images/ars_jersey.jpeg', 'Sport');

INSERT INTO `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`) 
VALUES ('Cleats', 'Nike Cleats', 100.00, 100, 'static/images/boot.jpeg', 'Sport');

INSERT INTO `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)  
VALUES ('Shin Guards', 'Nike Shin Guards', 50.00, 100, 'static/images/nike_guards.jpeg', 'Sport');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);

INSERT INTO `product_reviews` (`item_id`, `username`, `review_text`, `review_date`)
VALUES (1, 'user1', 'This product is amazing!', '2023-07-30 12:00:00');


INSERT INTO `rewards` (`reward_name`, `description`, `points_required`, `image_url`)
VALUES ('10% Discount Coupon', 'Get a 10% discount on your next purchase.', 100, 'static/images/nike_guards.jpeg');
INSERT INTO `rewards` (`reward_name`, `description`, `points_required`, `image_url`)
Values ('Free Shipping', 'Redeem this reward for free shipping on your order.', 150, 'static/images/nike_guards.jpeg');